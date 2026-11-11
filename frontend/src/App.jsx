import { useEffect, useState } from "react";
import {
  activateEmployee,
  createEmployee,
  deactivateEmployee,
  listEmployees,
  updateEmployeeNames,
} from "./api.js";

function missingNamesMessage(firstName, lastName) {
  const first = firstName.trim();
  const last = lastName.trim();
  if (!first && !last) {
    return "Enter a first name and a last name.";
  }
  if (!first) {
    return "Enter a first name.";
  }
  if (!last) {
    return "Enter a last name.";
  }
  return "";
}

export default function App() {
  const [employees, setEmployees] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [tableMessage, setTableMessage] = useState({ kind: "", text: "" });
  const [createOpen, setCreateOpen] = useState(false);
  const [createFirst, setCreateFirst] = useState("");
  const [createLast, setCreateLast] = useState("");
  const [createError, setCreateError] = useState("");
  const [editingId, setEditingId] = useState(null);
  const [editFirst, setEditFirst] = useState("");
  const [editLast, setEditLast] = useState("");

  async function refreshList() {
    const rows = await listEmployees();
    setEmployees(rows);
  }

  useEffect(() => {
    refreshList().catch(() => {
      setTableMessage({ kind: "failure", text: "Could not load employees." });
    });
  }, []);

  function openCreate() {
    setCreateFirst("");
    setCreateLast("");
    setCreateError("");
    setCreateOpen(true);
  }

  function closeCreate() {
    setCreateOpen(false);
    setCreateError("");
  }

  async function submitCreate(event) {
    event.preventDefault();
    const localMessage = missingNamesMessage(createFirst, createLast);
    if (localMessage) {
      setCreateError(localMessage);
      return;
    }
    try {
      await createEmployee(createFirst, createLast);
      await refreshList();
      closeCreate();
      setTableMessage({ kind: "success", text: "Employee created." });
    } catch (error) {
      setCreateError(error.message);
    }
  }

  function startEdit(employee, event) {
    event.stopPropagation();
    setSelectedId(employee.id);
    setEditingId(employee.id);
    setEditFirst(employee.firstName);
    setEditLast(employee.lastName);
  }

  function cancelEdit(event) {
    event.stopPropagation();
    setEditingId(null);
  }

  async function saveEdit(employee, event) {
    event.stopPropagation();
    event.preventDefault();
    const localMessage = missingNamesMessage(editFirst, editLast);
    if (localMessage) {
      setTableMessage({ kind: "failure", text: localMessage });
      return;
    }
    try {
      await updateEmployeeNames(employee.id, editFirst, editLast);
      await refreshList();
      setEditingId(null);
      setTableMessage({ kind: "success", text: "Employee name updated." });
    } catch (error) {
      setTableMessage({ kind: "failure", text: error.message });
    }
  }

  async function setStatus(employee, nextStatus, event) {
    event.stopPropagation();
    try {
      if (nextStatus === "Active") {
        await activateEmployee(employee.id);
      } else {
        await deactivateEmployee(employee.id);
      }
      await refreshList();
      setTableMessage({
        kind: "success",
        text:
          nextStatus === "Active"
            ? "Employee is Active."
            : "Employee is Inactive.",
      });
    } catch (error) {
      setTableMessage({ kind: "failure", text: error.message });
    }
  }

  return (
    <div className="page">
      <header className="brand-bar">Employee list</header>

      <div className="page-header">
        <button
          type="button"
          className="plus-button"
          aria-label="Add employee"
          data-testid="open-create"
          onClick={openCreate}
        >
          +
        </button>
      </div>

      <section className="list-region" aria-label="Employee list">
        {employees.length === 0 ? (
          <div className="empty" data-testid="empty-list">
            <h2>No employees yet.</h2>
            <p>Use + to add someone.</p>
          </div>
        ) : (
          <table data-testid="employee-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {employees.map((employee) => {
                const isEditing = editingId === employee.id;
                return (
                  <tr
                    key={employee.id}
                    data-testid={`employee-row-${employee.id}`}
                    className={
                      employee.id === selectedId ? "selected" : undefined
                    }
                    onClick={() => setSelectedId(employee.id)}
                  >
                    <td className="muted-id">{employee.id}</td>
                    <td>
                      {isEditing ? (
                        <input
                          value={editFirst}
                          onChange={(event) => setEditFirst(event.target.value)}
                          onClick={(event) => event.stopPropagation()}
                          aria-label="First name"
                        />
                      ) : (
                        employee.firstName
                      )}
                    </td>
                    <td>
                      {isEditing ? (
                        <input
                          value={editLast}
                          onChange={(event) => setEditLast(event.target.value)}
                          onClick={(event) => event.stopPropagation()}
                          aria-label="Last name"
                        />
                      ) : (
                        employee.lastName
                      )}
                    </td>
                    <td>
                      <span
                        className={
                          employee.status === "Active"
                            ? "chip chip-active"
                            : "chip chip-inactive"
                        }
                      >
                        {employee.status}
                      </span>
                    </td>
                    <td className="actions">
                      {isEditing ? (
                        <>
                          <button
                            type="button"
                            onClick={(event) => saveEdit(employee, event)}
                          >
                            Save
                          </button>
                          <button
                            type="button"
                            onClick={cancelEdit}
                          >
                            Cancel
                          </button>
                        </>
                      ) : (
                        <>
                          <button
                            type="button"
                            className="icon-button"
                            aria-label={`Edit ${employee.firstName} ${employee.lastName}`}
                            onClick={(event) => startEdit(employee, event)}
                          >
                            ✎
                          </button>
                          <button
                            type="button"
                            onClick={(event) =>
                              setStatus(employee, "Active", event)
                            }
                          >
                            Activate
                          </button>
                          <button
                            type="button"
                            onClick={(event) =>
                              setStatus(employee, "Inactive", event)
                            }
                          >
                            Deactivate
                          </button>
                        </>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
        {tableMessage.text ? (
          <p
            className={`table-message table-message-${tableMessage.kind}`}
            role="status"
            data-testid="outcome-banner"
          >
            {tableMessage.text}
          </p>
        ) : null}
      </section>

      {createOpen ? (
        <div className="overlay" onClick={closeCreate}>
          <form
            className="floating-box"
            data-testid="create-form"
            onClick={(event) => event.stopPropagation()}
            onSubmit={submitCreate}
          >
            <h2>Add employee</h2>
            <label>
              First name
              <input
                value={createFirst}
                onChange={(event) => setCreateFirst(event.target.value)}
                autoComplete="off"
                autoFocus
                data-testid="create-first-name"
              />
            </label>
            <label>
              Last name
              <input
                value={createLast}
                onChange={(event) => setCreateLast(event.target.value)}
                autoComplete="off"
                data-testid="create-last-name"
              />
            </label>
            {createError ? <p className="field-error">{createError}</p> : null}
            <div className="floating-actions">
              <button type="submit" data-testid="create-submit">
                Create
              </button>
              <button type="button" onClick={closeCreate}>
                Cancel
              </button>
            </div>
          </form>
        </div>
      ) : null}
    </div>
  );
}
