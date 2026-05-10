print("====== FINAL TEXT ANALYZER ======")
# Write text to file
file = open("text.txt", "w")
text = input("Enter text: ")
file.write(text)
file.close()
# Menu Function
def menu():
    print("\n1. Show Content")
    print("2. Word Count")
    print("3. Line Count")
    print("4. Character Count")
    print("5. Vowel Count")
    print("6. Search Word")
    print("7. Uppercase")
    print("8. Lowercase")
    print("9. Replace Word")
    print("10. Reverse Text")
    print("11. Exit")
# Main Loop
while True:
    menu()
    choice = input("Enter choice: ")
    # Read file
    file = open("text.txt", "r")
    data = file.read()
    file.close()
    if data == "":
        print("File is empty")
    elif choice == "1":
        print("\nContent:")
        print(data)
    elif choice == "2":
        print("Word count:", len(data.split()))
    elif choice == "3":
        print("Line count:", len(data.split("\n")))
    elif choice == "4":
        print("Character count:", len(data))
        print("Without spaces:", len(data.replace(" ", "")))
    elif choice == "5":
        count = 0
        for i in data:
            if i.lower() in "aeiou":
                count += 1
        print("Vowel count:", count)
    elif choice == "6":
        word = input("Enter word: ")
        print("Count:", data.lower().count(word.lower()))
    elif choice == "7":
        print(data.upper())
    elif choice == "8":
        print(data.lower())
    elif choice == "9":
        old = input("Old word: ")
        new = input("New word: ")
        new_data = data.replace(old, new)
        file = open("text.txt", "w")
        file.write(new_data)
        file.close()
        print("Word replaced successfully")
    elif choice == "10":
        print("Reverse text:")
        print(data[::-1])
    elif choice == "11":
        print("Project Ended")
        break
    else:
        print("Invalid choice")



