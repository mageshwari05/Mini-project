string = "learn python programming"

while True:
    print("\n1.word count \n2.vowels count \n3.exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("words count")
        count = 1
        for i in string:
            if i == " ":
                count = count + 1
        print("Count of words:", count)

    elif choice == 2:
        print("Vowels count")
        count = 0
        for i in string:
            if i in "aeiou":
                count = count + 1
        print("Count of vowels", count)

    elif choice == 3:
        print("Thank you")
        break

    else:
        print("invalid number")
