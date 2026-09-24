# OPTION 1 : Print the results directly

"""You cannot easily reuse the results elsewhere.
Harder to test because the output goes directly to the screen."""

def search_tasks(tasks, keyword):
    print("\n--- Search Results ---")

    for task in tasks:
        if keyword.lower() in task["description"].lower():
            print(f"{task['description']} [{task['status']}]")

# OPTION 2 : 

"""The caller decides what to do with the results.
Results can be displayed, counted, sorted, saved to a file, or processed further.
Easier to test."""

def search_tasks(tasks, keyword):
    matches = []

    for task in tasks:
        if keyword.lower() in task["description"].lower():
            matches.append(task)

    return matches