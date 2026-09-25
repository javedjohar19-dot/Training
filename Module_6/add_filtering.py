import json

class Task:
    """Represents a single task."""

    def __init__(
        self,
        description,
        status="pending",
        priority="medium",
        due_date=None
    ):
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "completed"

    def to_dict(self):
        """Convert the task into a dictionary."""
        return {
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary."""
        return cls(
            description=data["description"],
            status=data.get("status", "pending"),
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date")
        )

    def __str__(self):
        """Return a readable description of the task."""
        status_symbol = "✓" if self.status == "completed" else "○"

        result = (
            f"{status_symbol} {self.description} "
            f"[Priority: {self.priority}]"
        )

        if self.due_date:
            result += f" [Due: {self.due_date}]"

        return result


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self._load_tasks()

    def _load_tasks(self):
        """Load tasks from the JSON file into self.tasks."""
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)

            self.tasks = [
                Task.from_dict(task_data)
                for task_data in tasks_data
            ]

            print(
                f"Loaded {len(self.tasks)} task(s) "
                f"from {self.filename}."
            )

        except FileNotFoundError:
            print(
                "No save file found. "
                "Starting with an empty task list."
            )
            self.tasks = []

        except json.JSONDecodeError:
            print(
                "Save file is corrupted. "
                "Starting with an empty task list."
            )
            self.tasks = []

        except IOError as error:
            print(f"Error loading tasks: {error}")
            self.tasks = []

    def _save_tasks(self):
        """Save self.tasks to the JSON file."""
        tasks_data = [
            task.to_dict()
            for task in self.tasks
        ]

        try:
            with open(self.filename, "w") as file:
                json.dump(tasks_data, file, indent=4)

            print(
                f"Saved {len(self.tasks)} task(s) "
                f"to {self.filename}."
            )

        except IOError as error:
            print(f"Error saving tasks: {error}")

    def add_task(self):
        """Interactively add a new task."""
        description = input(
            "Enter the task description: "
        ).strip()

        if not description:
            print("Task description cannot be empty.")
            return

        priority = input(
            "Priority (high/medium/low) [medium\]: "
        ).strip().lower()

        if priority == "":
            priority = "medium"
        elif priority not in ("high", "medium", "low"):
            print("Invalid priority. Using medium.")
            priority = "medium"

        due_date = input(
            "Due date (YYYY-MM-DD) "
            "or press Enter for none: "
        ).strip()

        if due_date == "":
            due_date = None

        task = Task(
            description=description,
            priority=priority,
            due_date=due_date
        )

        self.tasks.append(task)
        self._save_tasks()

        print(f'Added: "{description}"')

    def view_tasks(self):
        """Display all tasks."""
        if len(self.tasks) == 0:
            print("Your task list is empty.")
            return

        print("\n--- Your Tasks ---")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

        print("------------------")

    def mark_task_complete(self):
        """Show tasks and let the user mark one as complete."""
        if len(self.tasks) == 0:
            print("No tasks to mark.")
            return

        self.view_tasks()

        task_number_str = input(
            "Enter the task number to mark complete: "
        ).strip()

        if not task_number_str.isdigit():
            print("Please enter a valid number.")
            return

        task_index = int(task_number_str) - 1

        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task number.")
            return

        selected_task = self.tasks[task_index]

        if selected_task.status == "completed":
            print("That task is already completed.")
            return

        selected_task.mark_complete()
        self._save_tasks()

        print(
            f'Marked "{selected_task.description}" '
            f"as completed."
        )

    def view_pending(self):
        """Display only pending tasks."""
        pending_tasks = [
        task for task in self.tasks
        if task.status == "pending"
        ]

        if len(pending_tasks) == 0:
            print("No pending tasks found.")
            return

        print("\n--- Pending Tasks ---")
        for index, task in enumerate(pending_tasks, start=1):
            print(f"{index}. {task}")
        print("---------------------")

    def delete_task(self):
        """Show tasks and let the user delete one."""
        if len(self.tasks) == 0:
            print("No tasks to delete.")
            return

        self.view_tasks()

        task_number_str = input(
            "Enter the task number to delete: "
        ).strip()

        if not task_number_str.isdigit():
            print("Please enter a valid number.")
            return

        task_index = int(task_number_str) - 1

        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task number.")
            return

        removed_task = self.tasks.pop(task_index)
        self._save_tasks()

        print(f'Deleted: "{removed_task.description}"')

    def run(self):
        """Run the interactive Task Manager."""
        print("=== Task Manager ===")

        while True:
            print("1. Add a task")
            print("2. View tasks")
            print("3. View pending tasks")
            print("4. Mark a task as complete")
            print("5. Delete a task")
            print("6. Exit")

            choice = input(
                "\nEnter your choice (1-6): "
            ).strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_pending()
            elif choice == "4":
                self.mark_task_complete()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self._save_tasks()
                print("Goodbye!")
                break
            else:
                print(
                    "Invalid choice. "
                    "Please enter 1, 2, 3, 4, 5 or 6."
                )


if __name__ == "__main__":
    app = TaskManager()
    app.run()