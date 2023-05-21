PRAGMA foreign_keys = ON;

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    project_id INTEGER NOT NULL,
    FOREIGN KEY(project_id) REFERENCES projects(id)
);

CREATE TABLE managers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    project_id INTEGER NOT NULL,
    FOREIGN KEY(project_id) REFERENCES projects(id)
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME
);

CREATE TABLE meetings (
    id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    datetime DATETIME NOT NULL,
    transcript VARCHAR(50) NOT NULL,
    manager_id INTEGER,
    employee_id INTEGER,
    project_id INTEGER NOT NULL,
    FOREIGN KEY(manager_id) REFERENCES managers(id),
    FOREIGN KEY(employee_id) REFERENCES employees(id),
    FOREIGN KEY(project_id) REFERENCES projects(id)
);

CREATE INDEX idx_meetings_manager_id ON meetings(manager_id);
CREATE INDEX idx_meetings_employee_id ON meetings(employee_id);
CREATE INDEX idx_meetings_project_id ON meetings(project_id);