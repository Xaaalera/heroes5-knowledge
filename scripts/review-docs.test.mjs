import { test } from 'node:test';
import assert from 'node:assert/strict';
import { documentationCriteria, validateDocsReview } from './review-docs.mjs';

const report = () => ({
  reviewer: 'test-reviewer',
  files: ['docs/example.md'],
  criteria: Object.fromEntries(documentationCriteria.map((criterion) => [
    criterion, { verdict: 'PASS', evidence: 'Fixture evidence for validator testing only.' },
  ])),
  findings: [],
});

test('a complete reasoned review covers its changed files', () => {
  assert.doesNotThrow(() => validateDocsReview(report(), ['docs/example.md']));
});
test('a score without an independent report fails', () => {
  assert.throws(() => validateDocsReview(undefined, []), /identity/);
});
test('omitted changed files fail', () => {
  assert.throws(() => validateDocsReview(report(), ['docs/missing.md']), /every changed/);
});
test('every criterion requires evidence and a passing disposition', () => {
  for (const criterion of documentationCriteria) {
    for (const replacement of [undefined, { verdict: 'PASS', evidence: '' }, { verdict: 'FAIL', evidence: 'Defect' }]) {
      const review = report();
      review.criteria[criterion] = replacement;
      assert.throws(() => validateDocsReview(review, review.files), new RegExp(criterion));
    }
  }
});
test('major and blocker findings prevent push', () => {
  for (const severity of ['major', 'blocker']) {
    const review = report();
    review.findings.push({ severity, path: review.files[0], detail: 'Confirmed defect' });
    assert.throws(() => validateDocsReview(review, review.files), /blocking/);
  }
});
test('minor and draft advisories remain visible without blocking', () => {
  const review = report();
  review.findings.push({ severity: 'advisory', path: review.files[0], detail: 'Known draft; not certified.' });
  assert.doesNotThrow(() => validateDocsReview(review, review.files));
});
test('findings cannot omit severity or reference an unreviewed path', () => {
  const review = report();
  review.findings = [{ severity: 'minor', path: 'unknown.md', detail: 'Defect' }];
  assert.throws(() => validateDocsReview(review, review.files), /reviewed path/);
  delete review.findings;
  assert.throws(() => validateDocsReview(review, review.files), /explicitly list/);
});
