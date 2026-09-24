"""The user is sent back to the main menu.
The user must choose the option again.
Can be frustrating if they make a small mistake."""

if not task_number.isdigit():
    print("Please enter a valid number.")
    return


# Another approch:Keep asking until input is valid

""" More professional
    More loops and control logic to manage
    Any situation where usability is important.
"""
while True:
    task_number = input("Enter the task number: ")

    if not task_number.isdigit():
        print("Please enter a valid number.")
        continue

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        continue

    break

# Current Code:
task_number = input("Enter the task number to delete: ")

if not task_number.isdigit():
    print("Please enter a valid number.")
    return

# improvement: replace with a loop
while True:
    task_number = input("Enter the task number to delete: ")

    if not task_number.isdigit():
        print("Please enter a valid number.")
        continue

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        continue

    break
