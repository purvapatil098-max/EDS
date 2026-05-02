lst = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter choice: ")

    if not choice.isdigit():
        print("Invalid choice")
        continue

    choice = int(choice)

    if choice == 1:   # Add
        val = input("Integer: ")
        if val.lstrip('-').isdigit():
            val = int(val)
            lst.append(val)
            print("List after adding:", lst)
        else:
            print("Invalid input")

    elif choice == 2:   # Remove
        if len(lst) == 0:
            print("List is empty")
        else:
            val = input("Integer: ")
            if val.lstrip('-').isdigit():
                val = int(val)
                if val in lst:
                    lst.remove(val)
                    print("List after removing:", lst)
                else:
                    print("Element not found")
            else:
                print("Invalid input")

    elif choice == 3:   # Display
        if len(lst) == 0:
            print("List is empty")
        else:
            print(lst )

    elif choice == 4:   # Quit
        break

    else:
        print("Invalid choice")
