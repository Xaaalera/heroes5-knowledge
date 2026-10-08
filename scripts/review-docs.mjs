import { createHash } from 'node:crypto';

export const articleCriticLenses = [
  'newcomer', 'accuracy', 'steps', 'structure', 'translation',
];

export const articleContentHash = (content) => createHash('sha256')
  .update(content.replace(/\r\n/g, '\n'), 'utf8').digest('hex');

export const validateArticleCritiques = (review, articles) => {
  if (articles.length === 0) {
    return;
  }
  if (!Array.isArray(review?.articleCritiques)) {
    throw new Error('Changed site articles require five independent critic records.');
  }
  for (const article of articles) {
    const matches = review.articleCritiques.filter((record) => record.path === article.path);
    if (matches.length !== 1) {
      throw new Error(`Article requires one current critique record: ${article.path}`);
    }
    const record = matches[0];
    if (record.sha256 !== articleContentHash(article.content)) {
      throw new Error(`Article critique is stale: ${article.path}`);
    }
    if (typeof record.author !== 'string' || !record.author.trim()
        || !Number.isInteger(record.round) || record.round < 1 || record.round > 3) {
      throw new Error(`Article critique requires an author and round 1–3: ${article.path}`);
    }
    if (!Array.isArray(record.critics) || record.critics.length !== articleCriticLenses.length) {
      throw new Error(`Article requires exactly five critic lanes: ${article.path}`);
    }
    const identities = new Set();
    for (const lane of articleCriticLenses) {
      const critics = record.critics.filter((critic) => critic.lane === lane);
      if (critics.length !== 1) {
        throw new Error(`Missing or duplicate article critic lane ${lane}: ${article.path}`);
      }
      const critic = critics[0];
      if (typeof critic.reviewer !== 'string' || !critic.reviewer.trim()
          || critic.reviewer.trim() === record.author.trim() || identities.has(critic.reviewer.trim())) {
        throw new Error(`Article critics must be independent of author and each other: ${article.path}`);
      }
      identities.add(critic.reviewer.trim());
      if (typeof critic.evidence !== 'string' || !critic.evidence.trim()
          || !Array.isArray(critic.findings)) {
        throw new Error(`Article critic requires evidence and explicit findings: ${article.path}`);
      }
      for (const finding of critic.findings) {
        if (!['S1', 'S2', 'S3'].includes(finding.severity)
            || !['open', 'resolved', 'refuted', 'unproven'].includes(finding.state)
            || typeof finding.location !== 'string' || !finding.location.trim()
            || typeof finding.problem !== 'string' || !finding.problem.trim()
            || typeof finding.consequence !== 'string' || !finding.consequence.trim()
            || typeof finding.evidence !== 'string' || !finding.evidence.trim()) {
          throw new Error(`Article finding requires location, failure, consequence, severity and evidence: ${article.path}`);
        }
        if (['S1', 'S2'].includes(finding.severity)
            && !['resolved', 'refuted'].includes(finding.state)) {
          throw new Error(`Article has an unresolved substantial finding: ${article.path}`);
        }
        if (['resolved', 'refuted'].includes(finding.state)
            && (typeof finding.disposition !== 'string' || !finding.disposition.trim()
              || typeof finding.verification !== 'string' || !finding.verification.trim())) {
          throw new Error(`Closed article finding requires a disposition and verification evidence: ${article.path}`);
        }
      }
    }
  }
};

export const documentationCriteria = [
  'purpose', 'structure', 'specificity', 'reproducibility',
  'evidence', 'applicability', 'translations', 'maintenance',
];

export const validateDocsReview = (review, files, score) => {
  if (!review || typeof review.reviewer !== 'string' || !review.reviewer.trim()) {
    throw new Error('Docs review requires the actual independent reviewer identity.');
  }
  if (!Array.isArray(review.files) || files.some((file) => !review.files.includes(file))) {
    throw new Error('Docs review must cover every changed Markdown file.');
  }
  for (const criterion of documentationCriteria) {
    const result = review.criteria?.[criterion];
    if (!result || !['PASS', 'N/A'].includes(result.verdict)
        || typeof result.evidence !== 'string' || !result.evidence.trim()) {
      throw new Error(`Docs review requires a reasoned PASS or N/A for ${criterion}.`);
    }
  }
  if (!Array.isArray(review.findings)) {
    throw new Error('Docs review must explicitly list findings, including an empty list.');
  }
  for (const finding of review.findings) {
    if (!['blocker', 'major', 'minor', 'advisory'].includes(finding.severity)
        || typeof finding.path !== 'string' || !review.files.includes(finding.path)
        || typeof finding.detail !== 'string' || !finding.detail.trim()) {
      throw new Error('Docs review finding requires severity, reviewed path and concrete detail.');
    }
    if (['blocker', 'major'].includes(finding.severity)) {
      throw new Error('Docs review has blocking findings. Fix and review the final diff again.');
    }
  }
  const expectedScore = Math.max(0, 10 - 3 * review.findings.filter((finding) => finding.severity === 'major').length
    - 20 * review.findings.filter((finding) => finding.severity === 'blocker').length
    - review.findings.filter((finding) => finding.severity === 'minor').length);
  if (score !== expectedScore) {
    throw new Error(`Docs score must match its findings: expected ${expectedScore}.`);
  }
};
