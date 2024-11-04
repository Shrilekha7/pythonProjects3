#contactManager.py
# Initialize an empty dictionary to store contacts
dic1 = dict()

# Function to store a new contact
def store_Contact(name, contactNo, email):
    dic1[name] = {"contactNo": contactNo, "email": email}  # Add name as key, contact number and email as values
    print(f"Contact added: {dic1}")

# Function to search for a contact by name
def search_Contact(name):
    if name in dic1:  # Check if the name exists in the contact list
        print(f"Name: {name} contact number: {dic1[name]['contactNo']}, email: {dic1[name]['email']}")
    else:
        print(f"{name} is not in the contact list")

# Function to update an existing contact
def update_Contact(name, Number, email):
    if name in dic1:  # Check if the name exists in the contact list
        dic1[name] = {"contactNo": Number, "email": email}  # Update contact number and email
        print(f"{name}'s contact updated to {Number}, email: {email}")
    else:
        print(f"{name} is not in the contact list")

# Function to view all contacts
def view_Contacts():
    if dic1:  # Check if there are any contacts stored
        print("Contacts:")
        for name, details in dic1.items():  # Iterate through the dictionary to print all contacts
            print(f"{name}: {details['contactNo']} ({details['email']})")
    else:
        print("No contacts found.")  # If no contacts exist, print a message

# Function to filter and display contacts that have Gmail addresses
def filter_Contacts():
    gmail_contacts = {name: details for name, details in dic1.items() if "gmail" in details["email"]}  # Filter by "gmail" in the email address
    if gmail_contacts:  # Check if any Gmail contacts exist
        print("Contacts with Gmail address:")
        for name, details in gmail_contacts.items():
            print(f"{name}: {details['contactNo']} ({details['email']})")
    else:
        print("No contacts with Gmail address found.")

# Validation function for contact numbers
def validate_contact_number(contactNo):
    """Ensure the contact number is a valid string of digits."""
    if contactNo.isdigit() and len(contactNo) >= 10:  # Check if contact number is at least 10 digits
        return True
    print("Please enter a valid 10-digit contact number.")
    return False

# Validation function for email addresses
def validate_email(email):
    """Simple validation to check for '@' and '.' in the email."""
    if "@" in email and "." in email:  # Check if email contains "@" and "."
        return True
    print("Invalid email format! Please enter a valid email.")
    return False

# Main loop to display menu and accept user input
while True:
    # Display options for the user
    print("\nEnter 1 to Store a Contact number")
    print("Enter 2 to Search a Contact number")
    print("Enter 3 to Update a Contact number")
    print("Enter 4 to View all Contacts")
    print("Enter 5 to Filter Contacts by Gmail address")
    print("Enter 0 to Exit")
    
    try:
        # Get user input and handle invalid input
        res = int(input("Enter a Number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if res == 1:  # Option 1: Store a contact
        name = input("Enter a name: ").capitalize()
        while True:
            if name.isalpha():  # Ensure the name is valid (alphabetic characters only)
                break
            else:
                print("Please enter a valid Name")

        contactNo = input("Enter a Contact Number: ")
        while not validate_contact_number(contactNo):  # Validate contact number
            contactNo = input("Enter a Contact Number: ")

        email = input("Enter an email address: ")
        while not validate_email(email):  # Validate email address
            email = input("Enter an email address: ")

        store_Contact(name, contactNo, email)  # Store the contact

    elif res == 2:  # Option 2: Search a contact
        name = input("Enter a Name to search: ").capitalize()
        while True:
            if name.isalpha():  # Ensure the name is valid (alphabetic characters only)
                break
            else:
                print("Please enter a valid Name")
        search_Contact(name)  # Search for the contact by name
    
    elif res == 3:  # Option 3: Update a contact
        name = input("Enter a Name whose Contact number you want to update: ").capitalize()
        while True:
            if name.isalpha():  # Ensure the name is valid (alphabetic characters only)
                break
            else:
                print("Please enter a valid Name")
        
        contactNo = input("Enter a new contact number: ")
        while not validate_contact_number(contactNo):  # Validate new contact number
            contactNo = input("Enter a new contact number: ")

        email = input("Enter a new email address: ")
        while not validate_email(email):  # Validate new email address
            email = input("Enter a new email address: ")

        update_Contact(name, contactNo, email)  # Update the contact

    elif res == 4:  # Option 4: View all contacts
        view_Contacts()  # Display all contacts
    
    elif res == 5:  # Option 5: Filter contacts with Gmail addresses
        filter_Contacts()  # Filter and display Gmail contacts

    elif res == 0:  # Option 0: Exit the program
        print("Exiting the program.")
        break
    
    else:
        print("Invalid input! Please enter 1, 2, 3, 4, 5, or 0.")  # Handle invalid menu options

    # Continuation logic to either exit or continue the program
    cont = input("Press 9 to continue or 0 to exit: ")
    if cont == '0':
        print("Exiting the program.")
        break
