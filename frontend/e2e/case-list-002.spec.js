/**
 * CASE-LIST-002 — Empty list is shown as empty (positive / empty)
 * Source: docs/quality-package/scenarios/list-and-display.md
 * Disposition: Automate (UI) / TEST-007
 *
 * Given no employees exist
 * When a user opens the tool
 * Then the page shows that the list is empty rather than appearing broken,
 * and the create form is still available
 */
import { test, expect } from "@playwright/test";

test("CASE-LIST-002 empty list shows empty state and create remains available", async ({
  page,
  request,
}) => {
  const list = await request.get("http://127.0.0.1:5000/employees");
  expect(list.ok()).toBeTruthy();
  expect(await list.json()).toEqual([]);

  await page.goto("/", { waitUntil: "networkidle" });
  await expect(page.getByTestId("empty-list")).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "No employees yet." }),
  ).toBeVisible();
  await expect(page.getByTestId("open-create")).toBeVisible();
  // Hold so the video captures the empty state (fast asserts alone look blank)
  await page.waitForTimeout(1500);

  await page.getByTestId("open-create").click();
  await expect(page.getByTestId("create-form")).toBeVisible();
  await expect(page.getByTestId("create-first-name")).toBeVisible();
  await expect(page.getByTestId("create-last-name")).toBeVisible();
  await page.waitForTimeout(1500);
});
