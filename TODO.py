print("TO DO LIST")

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        file = open("todo.txt", "a")
        file.write(task + "\n")
        file.close()
        print("Task Added")

    # View Tasks
    elif choice == "2":
        file = open("todo.txt", "r")
        tasks = file.readlines()
        file.close()

        for i in range(len(tasks)):
            print(i+1, tasks[i])

    # Delete Task
    elif choice == "3":
        file = open("todo.txt", "r")
        tasks = file.readlines()
        file.close()

        for i in range(len(tasks)):
            print(i+1, tasks[i])

        delete = int(input("Enter task number: "))
        tasks.pop(delete-1)

        file = open("todo.txt", "w")
        file.writelines(tasks)
        file.close()

        print("Task Deleted")

    # Clear All Tasks
    elif choice == "4":
        file = open("todo.txt", "w")
        file.close()
        print("All Tasks Cleared")

    # Exit
    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid choice")
