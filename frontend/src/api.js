export const API_ORIGIN = "http://127.0.0.1:5000";

async function readJson(response) {
  const body = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(body.message || "The request could not be completed.");
  }
  return body;
}

export async function listEmployees() {
  const response = await fetch(`${API_ORIGIN}/employees`);
  return readJson(response);
}

export async function createEmployee(firstName, lastName) {
  const response = await fetch(`${API_ORIGIN}/employees`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ firstName, lastName }),
  });
  return readJson(response);
}

export async function updateEmployeeNames(id, firstName, lastName) {
  const response = await fetch(`${API_ORIGIN}/employees/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ firstName, lastName }),
  });
  return readJson(response);
}

export async function activateEmployee(id) {
  const response = await fetch(`${API_ORIGIN}/employees/${id}/activate`, {
    method: "POST",
  });
  return readJson(response);
}

export async function deactivateEmployee(id) {
  const response = await fetch(`${API_ORIGIN}/employees/${id}/deactivate`, {
    method: "POST",
  });
  return readJson(response);
}
