/**
 * UI create happy path — add an employee and confirm it appears in the list.
 *
 * Traces scenario intent from:
 * - CASE-CRT-001 (create → Active row with system id) — UI observation
 * - CASE-ACC-003 (success outcome visible) — TEST-007 Automate (UI)
 *
 * Given the list starts empty
 * When the user creates Alex Smith via the create form
 * Then the list shows Alex Smith as Active and a success outcome is visible
 */
import { test, expect } from "@playwright/test";

test("create employee appears in the list as Active", async ({ page, request }) => {
  const before = await request.get("http://127.0.0.1:5000/employees");
  expect(before.ok()).toBeTruthy();
  expect(await before.json()).toEqual([]);

  await page.goto("/", { waitUntil: "networkidle" });
  await expect(page.getByTestId("empty-list")).toBeVisible();
  await page.waitForTimeout(800);

  await page.getByTestId("open-create").click();
  await expect(page.getByTestId("create-form")).toBeVisible();
  await expect(
    page.locator("#employee-id, [name='id'], [data-testid='create-id']"),
  ).toHaveCount(0);

  await page.getByTestId("create-first-name").click();
  await page.getByTestId("create-first-name").fill("Alex");
  await page.getByTestId("create-last-name").click();
  await page.getByTestId("create-last-name").fill("Smith");
  await expect(page.getByTestId("create-first-name")).toHaveValue("Alex");
  await expect(page.getByTestId("create-last-name")).toHaveValue("Smith");
  await page.waitForTimeout(600);

  const createResponsePromise = page.waitForResponse(
    (response) =>
      response.url().includes("/employees") &&
      response.request().method() === "POST",
  );
  await page.getByTestId("create-submit").click();
  // Fail fast if client-side validation blocked the fetch
  await expect(page.locator(".field-error")).toHaveCount(0);
  const createResponse = await createResponsePromise;
  expect(createResponse.status()).toBe(201);

  await expect(page.getByTestId("create-form")).toHaveCount(0, { timeout: 10_000 });
  await expect(page.getByTestId("employee-table")).toBeVisible();
  await expect(page.getByRole("cell", { name: "Alex", exact: true })).toBeVisible();
  await expect(page.getByRole("cell", { name: "Smith", exact: true })).toBeVisible();
  await expect(page.getByText("Active", { exact: true })).toBeVisible();
  await expect(page.getByTestId("outcome-banner")).toContainText(/created/i);

  const after = await request.get("http://127.0.0.1:5000/employees");
  const rows = await after.json();
  expect(rows).toHaveLength(1);
  expect(rows[0].firstName).toBe("Alex");
  expect(rows[0].lastName).toBe("Smith");
  expect(rows[0].status).toBe("Active");
  expect(typeof rows[0].id).toBe("number");

  await page.waitForTimeout(1500);
});
