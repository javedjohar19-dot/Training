# task_manager_v1.py
# Version 1: Start with default tasks and add more
tasks = ["Learn Python","Build a Task Manager"]

print("=== Task Manager ===")

# Display current tasks
print("\nCurrent tasks:")
print(tasks)

# Ask user to add a new task
new_task = input("\nEnter a new task:")
tasks.append(new_task)

# Display updated list
print("\nUpdated tasks:")
print(tasks)