import { test, expect } from '@playwright/test';

for (const width of [320, 390, 768, 1088, 1440]) {
  test(`homepage fits at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 1000 });
    await page.goto('./');
    await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
    await expect(
      page.getByRole('link', { name: /Собрать свой отряд/ }),
    ).toBeVisible();
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth > window.innerWidth,
    );
    expect(overflow).toBe(false);
    await page.screenshot({
      path: `test-results/home-${width}.png`,
      fullPage: true,
    });
  });
}

test('navigation, bilingual counterpart and code article work below the Pages prefix', async ({
  page,
}) => {
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto('./');
  await page.getByRole('link', { name: 'Моддерам', exact: true }).click();
  await expect(page).toHaveURL(
    /heroes5-knowledge\/modding\/getting-started\/$/,
  );
  await page
    .getByRole('link', { name: 'Проверка изменений', exact: true })
    .first()
    .click();
  await expect(page.locator('pre')).toContainText('Get-FileHash');
  await page.getByRole('link', { name: 'English version' }).click();
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(
    'Verifying a change',
  );
  await page.getByRole('link', { name: 'Русская версия' }).click();
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(
    'Как проверить изменение',
  );
});

test('mobile navigation can be opened and followed', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('./');
  await expect(page.locator('#site-navigation')).toBeHidden();
  await page.getByRole('button', { name: /Меню/ }).click();
  await expect(page.locator('#site-navigation')).toBeVisible();
  await page
    .locator('#site-navigation')
    .getByRole('link', { name: 'Игрокам' })
    .click();
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(
    'Перед первым модом',
  );
});

test('keyboard search opens, finds a document and preserves deployment paths', async ({
  page,
}) => {
  await page.goto('./');
  await page.keyboard.press('/');
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('searchbox').fill('XDB');
  await page
    .locator('.search-dialog__results')
    .getByRole('link', { name: /PAK, H5U, XDB/ })
    .click();
  await expect(page).toHaveURL(/heroes5-knowledge\/reference\/formats\/$/);
  await page.keyboard.press('/');
  await page.keyboard.press('Escape');
  await expect(page.getByRole('dialog')).toBeHidden();
});

test('search reports empty and unavailable results', async ({ page }) => {
  await page.goto('./');
  await page.keyboard.press('/');
  await page.getByRole('searchbox').fill('zzznomatchzz');
  await expect(page.getByRole('status')).toContainText('Ничего не найдено');
  await page.reload();
  await page.route('**/search/search_index.json', (route) => route.abort());
  await page.keyboard.press('/');
  await page.getByRole('searchbox').fill('XDB');
  await expect(page.getByRole('status')).toContainText('Поиск недоступен');
});

test('English homepage and article fit on a narrow viewport', async ({
  page,
}) => {
  await page.setViewportSize({ width: 320, height: 844 });
  await page.goto('en/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth > innerWidth,
    ),
  ).toBe(false);
  await page.goto('en/modding/verification/');
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(
    'Verifying a change',
  );
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth > innerWidth,
    ),
  ).toBe(false);
});


test('all eight backgrounds load as viewport backgrounds and survive reload and translation', async ({ page }) => {
  const routes = [
    ['./', 'haven'],
    ['players/getting-started/', 'sylvan'],
    ['players/installing-mods/', 'fortress'],
    ['modding/getting-started/', 'academy'],
    ['modding/verification/', 'dungeon'],
    ['reference/formats/', 'necropolis'],
    ['about/', 'stronghold'],
    ['contributing/', 'inferno'],
  ];
  for (const [route, faction] of routes) {
    await page.goto(route);
    const background = page.locator('.world-background');
    await expect(background).toHaveCSS('position', 'fixed');
    await expect(page.locator('body')).toHaveAttribute('data-faction', faction);
    await expect.poll(() => background.locator('img').evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
    await page.reload();
    await expect(page.locator('body')).toHaveAttribute('data-faction', faction);
    await page.getByRole('link', { name: 'English version' }).click();
    await expect(page.locator('body')).toHaveAttribute('data-faction', faction);
    await expect.poll(() => background.locator('img').evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
  }
});
