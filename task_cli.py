import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
        


def add_task(description):
    tasks = load_tasks()
    

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")
    
def list_tasks(filter_status=None):
    tasks = load_tasks()
    
    if len(tasks) == 0:
        print("No tasks found!")
        return

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
        if len(tasks) == 0:
            print(f"No {filter_status} tasks found!")
            return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def main():
    if len (sys.argv) < 2:
        print("Usage: python task_cli.py <command>")
        print("Commands: add, list, update, delete, mark-done, mark-in-process")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description")
            print("Usage: python task_cli.py add \"Buy groceries\"")
        else:
            add_task(sys.argv[2])
            
    elif command == "list":
        if len(sys.argv) < 3:
            list_tasks()
        else:
            list_tasks(sys.argv[2])
    else:
        print(f"Unknown command: {command}")

main() 

