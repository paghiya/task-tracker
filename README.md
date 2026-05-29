# Task Tracker CLI

A simple command-line task manager built with Python.

## Usage
```bash
python task_cli.py <command> [arguments]

## Commands

| Command | Description |
|---|---|
| `add "description"` | Add a new task |
| `list` | List all tasks |
| `list done` | List tasks by status (`done`, `todo`, `in-progress`) |
| `update <id> "new description"` | Update a task |
| `delete <id>` | Delete a task |
| `mark-done <id>` | Mark task as done |
| `mark-in-progress <id>` | Mark task as in-progress |
| `mark-todo <id>` | Mark task as todo |

## Examples

bash
python task_cli.py add "Buy groceries"
python task_cli.py list
python task_cli.py mark-done 1
python task_cli.py delete 2

## Data

Tasks are stored in `tasks.json` (auto-created on first run).


