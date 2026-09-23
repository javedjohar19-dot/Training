# Store tasks with a description and creation date

tasks = []

task1 = ["Study Python", "2026-09-23"]
task2 = ["Practice Git", "2026-09-24"]

tasks.append(task1)
tasks.append(task2)

print("Tasks:")
print(tasks)

print("\nFirst task description:")
print(tasks[0][0])

print("\nFirst task date:")
print(tasks[0][1])

""" # I stored each task as a list containing the description and date. 
    # While this works, it is difficult to remember what each index represents. 
    # For example, task[0] is the description and task[1] is the date. 
    # It is also easy to accidentally put the values in the wrong order, 
    # and adding more information such as priority or status would make the list harder to understand.
"""