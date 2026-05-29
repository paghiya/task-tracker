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
    new_id = max((t["id"] for t in tasks), default=0) + 1
    

    #if len(tasks) == 0: # Not efficient if the last task on the list is not the task with the last id as well
        #new_id = 1      # Like if you've removed id 3 (and you got 4 ids at the first place) by manual removal from .json
    #else:
        #new_id = tasks[-1]["id"] + 1
    

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

def delete_task(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return
    
    print(f"Error: Task {task_id} not found")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task["description"] = new_description
            task["updatedAt"] = now
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found!")
    
def mark_task(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print("Task not found!")    

def main():
    if len (sys.argv) < 2:
        print("Usage: python task_cli.py <command>")
        print("Commands: add, list, update, delete, mark-done, mark-in-progress")
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
            
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID")
        else:
            delete_task(int(sys.argv[2]))
            
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide a task ID")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])   
    
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID")
        else:
            mark_task(int(sys.argv[2]), "done")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID")
        else:
            mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-todo":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID")
        else:
            mark_task(int(sys.argv[2]), "todo")
  
    else:
        print(f"Unknown command: {command}")
        

main() 

