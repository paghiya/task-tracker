import unittest
import os
import sys

sys.path.insert(0, "C:/Users/User/task-tracker")

import task_cli
from task_cli import add_task, delete_task, update_task, mark_task, load_tasks, save_tasks

TEST_FILE = "test_tasks.json"

class TestTaskTracker(unittest.TestCase):

    def setUp(self):
        task_cli.TASKS_FILE = TEST_FILE
        save_tasks([])

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        add_task("Buy groceries")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Buy groceries")
        self.assertEqual(tasks[0]["status"], "todo")

    def test_delete_task(self):
        add_task("Task to delete")
        task_id = load_tasks()[0]["id"]
        delete_task(task_id)
        self.assertEqual(len(load_tasks()), 0)

    def test_delete_nonexistent(self):
        # حذف ID که وجود نداره نباید خطا بده
        delete_task(999)
        self.assertEqual(len(load_tasks()), 0)

    def test_update_task(self):
        add_task("Old description")
        task_id = load_tasks()[0]["id"]
        update_task(task_id, "New description")
        self.assertEqual(load_tasks()[0]["description"], "New description")

    def test_mark_done(self):
        add_task("Some task")
        task_id = load_tasks()[0]["id"]
        mark_task(task_id, "done")
        self.assertEqual(load_tasks()[0]["status"], "done")

    def test_mark_in_progress(self):
        add_task("Some task")
        task_id = load_tasks()[0]["id"]
        mark_task(task_id, "in-progress")
        self.assertEqual(load_tasks()[0]["status"], "in-progress")

    def test_mark_todo(self):
        add_task("Some task")
        task_id = load_tasks()[0]["id"]
        mark_task(task_id, "done")
        mark_task(task_id, "todo")
        self.assertEqual(load_tasks()[0]["status"], "todo")

    def test_multiple_tasks(self):
        add_task("Task 1")
        add_task("Task 2")
        add_task("Task 3")
        self.assertEqual(len(load_tasks()), 3)

    def test_ids_are_unique(self):
        add_task("Task 1")
        add_task("Task 2")
        tasks = load_tasks()
        ids = [t["id"] for t in tasks]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main()
