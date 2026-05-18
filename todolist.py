# To-Do List Manager with File Saving

import os

FILENAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
            continue
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        try:
            rm = int(input("Enter task number to mark complete: "))
            if 1 <= rm <= len(tasks):
                print(f"Removed: {tasks[rm-1]}")
                tasks.pop(rm-1)
                save_tasks(tasks)
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
