#Contact book (dict) 

contacts = {}

while True:

    print("\n----- Contact Book -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        contacts[name] = phone

        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        print("\nAll Contacts:")

        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")