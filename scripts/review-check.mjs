import { execFileSync, execSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import {
  evaluateGate,
  getCumulativeDiff,
  hashDiff,
  loadConfig,
  readAttestationFor,
  deriveOverall,
  resolveHeadSha,
  writeAttestation,
} from 'bladeforge-review-harness';

const rawConfig = JSON.parse(
  readFileSync('.claude/review.config.json', 'utf8'),
);
const baseArgument = process.argv.indexOf('--base');
const base = baseArgument < 0 ? rawConfig.base : process.argv[baseArgument + 1];
if (!base || base.startsWith('-')) {
  throw new Error('A valid Git base is required.');
}
execFileSync('git', ['rev-parse', '--verify', `${base}^{commit}`], {
  stdio: 'pipe',
});
const tracked = execFileSync('git', ['ls-files', '-z'], {
  encoding: 'utf8',
}).split('\0');
const forbidden = tracked.filter((path) =>
  /^(site|node_modules|\.local|\.venv)\//i.test(path),
);
if (forbidden.length > 0) {
  throw new Error(
    `Local game or generated files are tracked: ${forbidden.join(', ')}`,
  );
}
const diff = getCumulativeDiff(base);
const hash = hashDiff(diff);
const config = loadConfig();
if (process.argv.includes('--info')) {
  console.log(JSON.stringify({ base, hash, config }));
  process.exit(0);
}
const attestArgument = process.argv.indexOf('--attest');
const resultsPath =
  attestArgument < 0 ? null : process.argv[attestArgument + 1];
const results = resultsPath
  ? JSON.parse(readFileSync(resultsPath, 'utf8'))
  : null;
const attestation = results
  ? {
      diffHash: hash,
      commitSha: resolveHeadSha(),
      perAgent: results,
      overall: deriveOverall(results),
      timestamp: new Date().toISOString(),
    }
  : readAttestationFor(hash);
const gate = evaluateGate({
  hash,
  attestation,
  diff,
  secretAllowlist: config.secretAllowlist,
});
if (!gate.ok) {
  throw new Error(
    `Review blocked: attestation=${gate.attestationOk}; secret findings=${gate.secrets.length}. Run $project-review.`,
  );
}
for (const lens of config.agents.filter((agent) => agent.enabled !== false)) {
  const result = attestation.perAgent?.[lens.name];
  if (
    !result ||
    result.verdict !== 'PASS' ||
    !Number.isFinite(result.score) ||
    result.score < lens.threshold ||
    result.score > 10
  ) {
    throw new Error(`Missing or insufficient review result for ${lens.name}.`);
  }
}
execFileSync(
  'git',
  ['merge-base', '--is-ancestor', attestation.commitSha, 'HEAD'],
  { stdio: 'pipe' },
);
for (const configuredGate of rawConfig.gates ?? []) {
  execSync(configuredGate.command, { stdio: 'inherit' });
}
if (results) {
  writeAttestation(attestation);
}
console.log(
  'Review passed: configured lenses, secrets, tracked files and deterministic checks.',
);
