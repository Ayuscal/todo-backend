# Simple To-Do List App

# Empty list to store tasks
tasks = []

def show_menu():
    print("\nSimple To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input(eval("Enter your choice (1-4): "))

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                del_index = int(input("Enter the task number to delete: "))
                removed = tasks.pop(del_index - 1)
                print(f"Deleted: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
