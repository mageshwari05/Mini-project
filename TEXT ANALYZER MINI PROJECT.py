print("TEXT ANALYZER PROJECT")
# Write data to file
file = open("text.txt","w")
text = input("Enter text: ")
file.write(text)
file.close()
while True:
    print("\n1. Show Content")
    print("2. Word Count")
    print("3. Line Count")
    print("4. Character Count")
    print("5. Vowel Count")
    print("6. Search Word")
    print("7. Uppercase")
    print("8. Lowercase")
    print("9. Replace Word")
    print("10. Exit")
    choice = input("Enter choice: ")
    file = open("text.txt","r")
    data = file.read()
    file.close()

    if choice == "1":
        print(data)

    elif choice == "2":
        print("Word count:", len(data.split()))

    elif choice == "3":
        print("Line count:", len(data.split("\n")))

    elif choice == "4":
        print("Character count:", len(data))

    elif choice == "5":
        count = 0
        for i in data:
            if i.lower() in "aeiou":
                count += 1
        print("Vowels:", count)

    elif choice == "6":
        word = input("Enter word: ")
        print("Count:", data.count(word))

    elif choice == "7":
        print(data.upper())

    elif choice == "8":
        print(data.lower())

    elif choice == "9":
        old = input("Old word: ")
        new = input("New word: ")
        print(data.replace(old, new))

    elif choice == "10":
        print("Exit")
        break

    else:
        print("Invalid choice")
