import { defineConfig, devices } from "@playwright/test";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const e2eDbPath = path.join(rootDir, "backend", "data", "playwright-e2e.db");
const backendPython = path.join(rootDir, "backend", ".venv", "bin", "python");
// One folder per Playwright invocation so videos are never overwritten
const runId = new Date().toISOString().replace(/[:.]/g, "-");
const outputDir = path.join("test-results", `run-${runId}`);

// Fresh empty store before webServer starts Flask
fs.mkdirSync(path.dirname(e2eDbPath), { recursive: true });
if (fs.existsSync(e2eDbPath)) {
  fs.unlinkSync(e2eDbPath);
}

export default defineConfig({
  testDir: "./e2e",
  outputDir,
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: 0,
  workers: 1,
  reporter: "list",
  preserveOutput: "always",
  use: {
    baseURL: "http://localhost:5173",
    viewport: { width: 1280, height: 720 },
    video: {
      mode: "on",
      size: { width: 1280, height: 720 },
    },
    trace: "on-first-retry",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  webServer: [
    {
      command: `${backendPython} app.py`,
      cwd: path.join(rootDir, "backend"),
      url: "http://127.0.0.1:5000/health",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
      env: {
        ...process.env,
        EMPLOYEE_DATABASE_PATH: e2eDbPath,
      },
    },
    {
      command: "npm run dev -- --host localhost --port 5173",
      cwd: path.join(rootDir, "frontend"),
      url: "http://localhost:5173",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
    },
  ],
});
