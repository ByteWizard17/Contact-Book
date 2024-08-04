# Initialize an empty dictionary to store contacts
contacts = {}

# Function to display the menu
def menu():
    print("--------------------MENU----------------------")
    print("Press 4 if you want to terminate the program.")
    print("Press 0 to look up an existing number.")
    print("Press 1 to add a person to the contact book.")
    print("Press 2 to update an existing number.")
    print("Press 3 to delete an existing number.")
    print("Press 5 to print all contacts.")
    print("Press any number from 6-9 to display the menu.")
    print("----------------------------------------------")
    print("           DIGITAL CONTACT BOOK              ")

# Function to display all contacts
def display():
    if contacts:
        for name, details in contacts.items():
            print(f"{name} : {details}")
    else:
        print("No contacts to display.")

# Display the menu initially
menu()

# Loop to continuously prompt the user for actions
while True:
    try:
        choice = int(input("Enter command: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        look = input("Enter the name of the number owner: ").upper()
        if look in contacts:
            print(f"Number of {look}: {contacts[look]}")
        else:
            print("Contact not found.")
    
    elif choice == 1:
        name = input("Enter the name of the new contact: ").upper()
        number = input("Enter an 11 or 8 digit number: ")
        if number.isdigit() and (len(number) == 11 or len(number) == 8):
            contact_type = "Mobile" if len(number) == 11 else "Landline"
            contacts[name] = [number, contact_type]
            print("              CONTACTS")
            display()
        else:
            print("Number is invalid. Please try again.")
    
    elif choice == 2:
        name = input("Enter the name of the person to update contact: ").upper()
        if name in contacts:
            number = input("Enter the new contact number (11 or 8 digits): ")
            if number.isdigit() and (len(number) == 11 or len(number) == 8):
                contact_type = "Mobile" if len(number) == 11 else "Landline"
                contacts[name] = [number, contact_type]
                print("              CONTACTS")
                display()
            else:
                print("Number is invalid. Please try again.")
        else:
            print("Contact not found.")
    
    elif choice == 3:
        name = input("Enter the name of the contact to remove: ").upper()
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} removed.")
            print("              CONTACTS")
            display()
        else:
            print("Contact not found.")
    
    elif choice == 4:
        print("Thank you for using the Digital Contact Book!")
        break
    
    elif choice == 5:
        print("              CONTACTS")
        display()
    
    else:
        menu()
