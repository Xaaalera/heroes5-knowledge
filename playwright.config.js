import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: 'tests',
  workers: 1,
  reporter: 'list',
  use: {
    baseURL: 'http://127.0.0.1:8768/heroes5-knowledge/',
    browserName: 'chromium',
    trace: 'retain-on-failure',
  },
  webServer: {
    command: 'python -m mkdocs serve --no-livereload --dev-addr 127.0.0.1:8768',
    url: 'http://127.0.0.1:8768/heroes5-knowledge/',
    reuseExistingServer: !process.env.CI,
  },
});
