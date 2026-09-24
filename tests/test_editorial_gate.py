"""Filesystem integration checks for the editorial gate; no game/browser needed."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

import yaml

MODULE = Path(__file__).resolve().parents[1] / 'scripts' / 'check_site.py'
SPEC = importlib.util.spec_from_file_location('check_site', MODULE)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class EditorialGateTests(unittest.TestCase):
    def validate(self, ru_changes=None, en_changes=None, raw=None):
        with tempfile.TemporaryDirectory() as folder:
            docs = Path(folder)
            for language, changes in [('ru', ru_changes), ('en', en_changes)]:
                metadata = dict(lang=language, translation='en/' if language == 'ru' else '',
                                content_type='reference', status='draft', faction='haven')
                metadata.update(changes or {})
                path = docs / ('en/index.md' if language == 'en' else 'index.md')
                path.parent.mkdir(parents=True, exist_ok=True)
                content = '---\n' + yaml.safe_dump(metadata) + '---\n# Example\n'
                path.write_text(raw if raw is not None and language == 'ru' else content, encoding='utf-8')
            return CHECK.check_articles(docs, {'haven'})

    def test_drafts_are_counted_without_claiming_verification(self):
        failures, counts = self.validate()
        self.assertEqual(failures, [])
        self.assertEqual(counts, dict(draft=2, verified=0, outdated=0))

    def test_complete_verified_pair_is_accepted(self):
        evidence = dict(status='verified', scope='Explicit test build',
                        verified_on='2020-01-01', sources=['https://example.org/evidence'])
        failures, counts = self.validate(evidence, evidence)
        self.assertEqual(failures, [])
        self.assertEqual(counts['verified'], 2)

    def test_unsupported_verified_claim_is_blocked(self):
        failures, _ = self.validate(dict(status='verified'), dict(status='verified'))
        for required in ('scope', 'verified_on', 'sources'):
            self.assertTrue(any(required in failure for failure in failures), required)

    def test_invalid_evidence_is_blocked(self):
        evidence = dict(status='verified', scope=' ', verified_on='9999-01-01', sources=['file:///private'])
        failures, _ = self.validate(evidence, evidence)
        for required in ('scope', 'verified_on', 'sources'):
            self.assertTrue(any(required in failure for failure in failures), required)

    def test_translation_cannot_point_to_itself_or_other_article(self):
        for target in ('', '../', 'en/other/'):
            with self.subTest(target=target):
                failures, _ = self.validate(dict(translation=target))
                self.assertTrue(any('reciprocal' in failure for failure in failures))

    def test_inconsistent_pair_and_invalid_fields_are_blocked(self):
        failures, _ = self.validate(dict(status='outdated', content_type='meta'), dict(faction='missing'))
        self.assertTrue(any('disagrees on status' in failure for failure in failures))
        self.assertTrue(any('invalid faction' in failure for failure in failures))
        failures, _ = self.validate(dict(status=['draft'], content_type=None, lang='en'))
        self.assertTrue(any('invalid status' in failure for failure in failures))
        self.assertTrue(any('invalid content_type' in failure for failure in failures))
        self.assertTrue(any('lang must' in failure for failure in failures))

    def test_invalid_frontmatter_is_reported(self):
        for raw in ('# Missing metadata', '---\n[bad: yaml\n---\n', '---\n- list\n---\n'):
            with self.subTest(raw=raw):
                failures, _ = self.validate(raw=raw)
                self.assertTrue(any('invalid YAML' in failure for failure in failures))


    def test_agent_index_rejects_a_removed_markdown_source(self):
        with tempfile.TemporaryDirectory() as folder:
            repository = Path(folder)
            source = repository / 'docs/topic.md'
            source.parent.mkdir()
            source.write_text('# Topic', encoding='utf-8')
            index = repository / 'llms.txt'
            index.write_text('# Index\n\n- [Topic](https://raw.githubusercontent.com/Xaaalera/heroes5-knowledge/main/docs/topic.md)\n', encoding='utf-8')
            self.assertEqual(CHECK.check_agent_index(index, repository), [])
            source.unlink()
            self.assertTrue(any('does not exist' in message for message in CHECK.check_agent_index(index, repository)))

    def test_agent_index_requires_a_published_file_and_confined_sources(self):
        with tempfile.TemporaryDirectory() as folder:
            repository = Path(folder)
            index = repository / 'llms.txt'
            self.assertTrue(CHECK.check_agent_index(index, repository))
            index.write_text('# Index\n\n- [Outside](https://raw.githubusercontent.com/Xaaalera/heroes5-knowledge/main/../outside.md)\n', encoding='utf-8')
            self.assertTrue(CHECK.check_agent_index(index, repository))


if __name__ == '__main__':
    unittest.main()
