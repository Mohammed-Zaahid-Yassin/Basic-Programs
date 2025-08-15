contacts = {}
while True:
    print("\nContact Book Options:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved!")
    elif choice == "2":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print("Contact not found.")
    elif choice == "3":      
        if not contacts:
            print("No contacts yet.")
        else:
            print("Contacts list:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
