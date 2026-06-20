contacts = []

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            print("\nContact List:")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("-" * 20)

    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False
        for contact in contacts:
            if contact["name"] == search or contact["phone"] == search:
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact Not Found!")

    elif choice == "4":
        phone = input("Enter Phone Number of Contact to Update: ")

        found = False
        for contact in contacts:
            if contact["phone"] == phone:
                contact["name"] = input("Enter New Name: ")
                contact["phone"] = input("Enter New Phone: ")
                contact["email"] = input("Enter New Email: ")
                contact["address"] = input("Enter New Address: ")

                print("Contact Updated Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == "5":
        phone = input("Enter Phone Number to Delete: ")

        found = False
        for contact in contacts:
            if contact["phone"] == phone:
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
