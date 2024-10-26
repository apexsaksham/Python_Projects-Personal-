contact = {}


while True:
    print("\nContact Book ")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Countate contact")
    print("7. Exit")


    choice = input("Enter your Choice : ")

    if choice == '1':
        name = input("Enter the name : ")
        if name in contact:
            print(f"Contact name {name} already exists")

        else:
            age = input("Enter age : ")
            email = input("Enter Email : ")
            mobile = input("Enter Mobile no. : ")
            contact[name] = {'age': int(age), 'email':email, 'mobile' : mobile } 
            print(f"Contact {name} has been Created")

    elif choice == '2':
        name = input("Enter the name you want to display : ")
        if name in contact:
            contacts = contact[name]
            print(f'Name:{name}, Age : {age}, Mobile No. : {mobile}' )

        else:
            print(f"Contact not found")

    elif choice == '3':
        name = input("Enter the name of contact you want to update : ")
        if name in contact:
            age = input("Enter updated age : ")
            email = input("Enter updated Email : ")
            mobile = input("Enter updated Mobile no. : ")
            contact[name] = {'age': int(age), 'email':email, 'mobile' : mobile } 

        else:
            print("Contact not found")

    elif choice == '4':
        name = input("Enter the contact name you want to delete : ")
        if name  in contact:
            del contact[name]
            print(f"Contact is Sucessfully deleted")

        else:
            print("Contact not found")


    elif choice == '5':
        search_name = input("Enter the name you want to search : ")
        found = False
        for name, contacts in contact.items():
            if search_name.lower() in name:
                print(f"Found - Name : {name}, Age : {age}, Email {email}, Mobile : {mobile}")
                found = True

            else:
                print("No contact found")

    elif choice == '6':
        print(f"Total contacts in your Book : {len(contact)}")

    
    elif choice == '7':
         print("Closing the Book..........")
         break
    
    else:
        print("Invalid input")