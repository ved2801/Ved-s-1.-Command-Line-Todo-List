import json
import os

FILENAME = "todos.json"

def load_tasks():
    """Load tasks from the JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """Display all current tasks with their completion status."""
    if not tasks:
        print("\nYour to-do list is empty!\n")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")
    print("-" * 23 + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    title = input("\nEnter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!\n")
    else:
        print("Task description cannot be empty.\n")

def complete_task(tasks):
    """Mark a specific task as complete."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[choice - 1]['title']}' marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """Main application loop."""
    tasks = load_tasks()
    while True:
        print("=== TODO APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
