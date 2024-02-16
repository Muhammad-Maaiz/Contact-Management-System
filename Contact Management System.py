# Contact Management System:

# Function to display the main menu
def display_menu():
    print("\n")
    print("Main Menu:".center(22))
    print("-" * 23)
    print("1.Add Contact")
    print("2.Display All Contacts")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    print("-" * 23)

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter your name: ").lower()
    # Check if contact already exists
    for contact in contacts:
        if contact[0] == name:
            print("Contact already exists!")
            return 
    phone_number = input("Enter your Phone Number: ")
    # Validate phone number
    if not phone_number.isdigit() or len(phone_number) != 11:
        print("Invalid phone number! Please enter a 11-digits Phone Number.")
        return 
    email_address = input("Enter your email address: ")
    # Validate email address
    if "@gmail.com" not in email_address:
        print("Invalid email address! Please enter a valid email.")
        return
    contact = name, phone_number, email_address
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts
def display_all_contact():
    # Check if there are no contacts
    if not contacts:
        print("No contacts in the list")
    else:
        # Display all contacts with index
        for index, contact in enumerate(contacts, start=1):
            print(index, contact)

# Function to search for a contact
def search_contact():
    search_name = input("Enter the name to search: ").lower()
    # Iterate over contacts to find the matching name
    for contact in contacts:
        if contact[0] == search_name:
            # Display contact details if found
            print("Contact Details:")
            print("Name:", contact[0])
            print("Phone Number:", contact[1])
            print("Email Address:", contact[2])
            return  
    else:
        # Inform user if contact not found
        print("Contact not found!")

# Function to delete a contact
def delete_contact():
    delete_name = input("Enter the name you want to delete: ").lower()
    # Iterate over contacts to find the matching name
    for contact in contacts:
        if contact[0] == delete_name:
            # Remove contact if found
            contacts.remove(contact)
            print("Contact Deleted successfully!")
            return
    else:
        # Inform user if contact not found
        print("Contact Not Found")

# Main program loop
while True:
    # Display the menu
    display_menu()
    try:
        # Get user choice
        choice = int(input("\nEnter your choice: "))
        
        # Perform actions based on user choice
        if choice == 1:
            add_contact()
        elif choice == 2:
            display_all_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Exiting the Program!")
            break
        else:
            print("Invalid Choice, Please enter a number between 1 to 5")
    except ValueError: # Error Handling for user bad response
        print("Enter a valid Integer")