to_do_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if not to_do_list:
        print("\nNo tasks in the list.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    try:
        view_tasks()
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(to_do_list):
            removed_task = to_do_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
