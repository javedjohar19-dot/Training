# task_manager_v1.py
# Version 1: Store tasks in a list, add one, display them all.
tasks = ["Learn Python","Build a Task Manager"]

print("=== Task Manager ===")
print("\nYour tasks:")
print(tasks)

first_task = input("Enter your task: ")
tasks.append(first_task)

second_task = input("Enter your task: ")
tasks.append(second_task)

third_task = input("Enter your task: ")
tasks.append(third_task)

print("\nYour new tasks:")
print(tasks)