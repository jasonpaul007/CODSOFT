# To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter task number to update: "))
            
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print("Deleted task:", removed_task)
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
