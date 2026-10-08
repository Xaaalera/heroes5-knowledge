import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, renameSync, unlinkSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { documentationCriteria, validateDocsReview, validateArticleCritiques } from './review-docs.mjs';

const validate = (review, files, score = 10) => validateDocsReview(review, files, score);

const report = () => ({
  reviewer: 'test-reviewer',
  files: ['docs/example.md'],
  criteria: Object.fromEntries(documentationCriteria.map((criterion) => [
    criterion, { verdict: 'PASS', evidence: 'Fixture evidence for validator testing only.' },
  ])),
  findings: [],
});

const article = { path: 'docs/example.md', content: '# Example\n\nReader task.\n' };
const articleReport = () => ({
  articleCritiques: [{
    path: article.path,
    sha256: createHash('sha256').update(article.content).digest('hex'),
    author: 'fixture-author',
    round: 2,
    critics: ['newcomer', 'accuracy', 'steps', 'structure', 'translation'].map((lane) => ({
      lane, reviewer: `fixture-critic-${lane}`,
      evidence: `Independent fixture evidence for ${lane}, validator testing only.`,
      findings: [],
    })),
  }],
});

test('article Git selection covers nested edits, additions and renames, excluding deletions and nonarticles', () => {
  const directory = mkdtempSync(join(tmpdir(), 'article-gate-'));
  const git = (...argumentsList) => execFileSync('git', argumentsList, { cwd: directory, encoding: 'utf8' }).trim();
  try {
    git('init', '--quiet');
    git('config', 'user.name', 'Gate fixture');
    git('config', 'user.email', 'fixture@example.invalid');
    git('config', 'commit.gpgsign', 'false');
    git('config', 'core.hooksPath', join(directory, 'disabled-hooks'));
    mkdirSync(join(directory, 'docs/en/reference'), { recursive: true });
    for (const path of ['docs/en/reference/edit.md', 'docs/remove.md', 'docs/rename.md', 'README.md']) {
      writeFileSync(join(directory, path), `# ${path}\nUnique fixture content.\n`);
    }
    git('add', '.');
    git('commit', '--quiet', '-m', 'Fixture policy adoption');
    const adoption = git('rev-parse', 'HEAD');
    writeFileSync(join(directory, 'docs/en/reference/edit.md'), '# Changed nested article\n');
    writeFileSync(join(directory, 'docs/new.md'), '# New article\n');
    writeFileSync(join(directory, 'README.md'), '# Changed repository entry\n');
    writeFileSync(join(directory, 'docs/data.json'), '{}');
    unlinkSync(join(directory, 'docs/remove.md'));
    renameSync(join(directory, 'docs/rename.md'), join(directory, 'docs/renamed.md'));
    git('add', '.');
    git('commit', '--quiet', '-m', 'Fixture changed articles');
    const selected = git('diff', '--name-only', '--diff-filter=AMR', '-z', adoption, 'HEAD', '--', 'docs/*.md').split('\0').filter(Boolean).sort();
    assert.deepEqual(selected, ['docs/en/reference/edit.md', 'docs/new.md', 'docs/renamed.md']);
    assert.equal(git('diff', '--name-only', '--diff-filter=AMR', '-z', 'HEAD', 'HEAD', '--', 'docs/*.md'), '');
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});

test('each current article requires all five independent critic lanes', () => {
  assert.doesNotThrow(() => validateArticleCritiques(articleReport(), [article]));
  assert.throws(() => validateArticleCritiques({}, [article]), /five independent/);
  const review = articleReport();
  review.articleCritiques[0].critics.pop();
  assert.throws(() => validateArticleCritiques(review, [article]), /exactly five/);
  assert.throws(() => validateArticleCritiques(articleReport(), [article, { ...article, path: 'docs/new.md' }]), /current critique/);
});

test('an edit invalidates old article critique but CRLF does not', () => {
  assert.throws(() => validateArticleCritiques(articleReport(), [{ ...article, content: article.content + 'New claim.' }]), /stale/);
  assert.doesNotThrow(() => validateArticleCritiques(articleReport(), [{ ...article, content: article.content.replace(/\n/g, '\r\n') }]));
});

test('one critic cannot represent multiple lanes or review their own article', () => {
  for (const replacement of ['fixture-author', ' fixture-author ', 'fixture-critic-newcomer', ' fixture-critic-newcomer ', '']) {
    const review = articleReport();
    review.articleCritiques[0].critics[1].reviewer = replacement;
    assert.throws(() => validateArticleCritiques(review, [article]), /independent/);
  }
  const review = articleReport();
  review.articleCritiques[0].critics[1].lane = 'newcomer';
  assert.throws(() => validateArticleCritiques(review, [article]), /duplicate/);
});

test('critic reports cannot exceed three rounds or omit evidence', () => {
  for (const round of [0, 4, '2']) {
    const review = articleReport();
    review.articleCritiques[0].round = round;
    assert.throws(() => validateArticleCritiques(review, [article]), /round 1/);
  }
  const review = articleReport();
  review.articleCritiques[0].critics[0].evidence = '';
  assert.throws(() => validateArticleCritiques(review, [article]), /evidence/);
});

test('substantial open or unproven defects block article publication', () => {
  for (const severity of ['S1', 'S2']) {
    for (const state of ['open', 'unproven']) {
      const review = articleReport();
      review.articleCritiques[0].critics[0].findings = [{
        severity, state, location: 'First procedure', problem: 'Missing required action', consequence: 'Reader cannot complete the task.', evidence: 'Concrete fixture evidence.',
      }];
      assert.throws(() => validateArticleCritiques(review, [article]), /unresolved substantial/);
    }
  }
  const review = articleReport();
  review.articleCritiques[0].critics[0].findings = [{
    severity: 'S2', state: 'resolved', location: 'First procedure', problem: 'Original missing action', consequence: 'Reader could not complete the task.', evidence: 'Original omission checked.', disposition: 'Required action added.', verification: 'Independent critic repeated the revised procedure.',
  }];
  assert.doesNotThrow(() => validateArticleCritiques(review, [article]));
  for (const field of ['consequence', 'disposition', 'verification']) {
    const incomplete = structuredClone(review);
    delete incomplete.articleCritiques[0].critics[0].findings[0][field];
    assert.throws(() => validateArticleCritiques(incomplete, [article]), /consequence|disposition and verification/);
  }
});

test('a complete reasoned review covers its changed files', () => {
  assert.doesNotThrow(() => validate(report(), ['docs/example.md']));
});
test('a score without an independent report fails', () => {
  assert.throws(() => validate(undefined, []), /identity/);
});
test('omitted changed files fail', () => {
  assert.throws(() => validate(report(), ['docs/missing.md']), /every changed/);
});
test('every criterion requires evidence and a passing disposition', () => {
  for (const criterion of documentationCriteria) {
    for (const replacement of [undefined, { verdict: 'PASS', evidence: '' }, { verdict: 'FAIL', evidence: 'Defect' }]) {
      const review = report();
      review.criteria[criterion] = replacement;
      assert.throws(() => validate(review, review.files), new RegExp(criterion));
    }
  }
});
test('major and blocker findings prevent push', () => {
  for (const severity of ['major', 'blocker']) {
    const review = report();
    review.findings.push({ severity, path: review.files[0], detail: 'Confirmed defect' });
    assert.throws(() => validate(review, review.files), /blocking/);
  }
});
test('draft advisories remain visible without blocking', () => {
  const review = report();
  review.findings.push({ severity: 'advisory', path: review.files[0], detail: 'Known draft; not certified.' });
  assert.doesNotThrow(() => validate(review, review.files));
});
test('findings cannot omit severity or reference an unreviewed path', () => {
  const review = report();
  review.findings = [{ severity: 'minor', path: 'unknown.md', detail: 'Defect' }];
  assert.throws(() => validate(review, review.files), /reviewed path/);
  delete review.findings;
  assert.throws(() => validate(review, review.files), /explicitly list/);
});

test('minor findings deduct points and cannot hide behind a passing score', () => {
  const review = report();
  review.findings = [{ severity: 'minor', path: review.files[0], detail: 'Concrete minor defect.' }];
  assert.doesNotThrow(() => validate(review, review.files, 9));
  assert.throws(() => validate(review, review.files, 10), /expected 9/);
  review.findings.push(...review.findings, ...review.findings);
  assert.throws(() => validate(review, review.files, 10), /expected 7/);
  assert.doesNotThrow(() => validate(review, review.files, 7));
});
