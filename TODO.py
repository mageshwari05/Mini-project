print("TO DO LIST")

print("1. Add Task")
print("2. View Tasks")
print("3. Exit")

choice = input("Enter choice: ")

if choice == "1":
    task = input("Enter task: ")
    file = open("TODO.txt","a")
    file.write(task + "\n")
    file.close()
    print("Task Added")

elif choice == "2":
    file = open("TODO.txt","r")
    print(file.read())
    file.close()

elif choice == "3":
    print("Exit")

else:
    print("Invalid choice")
