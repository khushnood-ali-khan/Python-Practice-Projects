#                            Contact Book ⭐⭐⭐⭐
# Create a contact manager.

# Each contact contains:
# Name
# Phone
# Email

# Menu:
# 1 Add Contact
# 2 View Contacts
# 3 Search Contact
# 4 Delete Contact
# 5 Exit

# Store contacts in a dictionary.

import json

contact_info = "ContactDetails.json"

def select_operation():
    while True:
        operation = input("SELECT YOUR OPERATION: ").strip()
        if operation.isdigit():
            operation = int(operation)
            if operation <= 4:
                return operation
            else:
                print("Invalid Operation")
        else:
            print("Enter the number only.")
        
def add_contact():
    contact_info["name"] = input("\n Name: ")
    while True:
        phone_no = input("Ph_no: ")
        if phone_no.isdigit():
            contact_info["phone"] = phone_no
            break
        else:
            print("Ph_No can only be digits.")
    contact_info["email"] = input("Email: ")


def view_contact():
    try:
        with open(contact_info, "r") as file:
            return json.load(file)
    except:
        return "No Contect Found."

def Search_contact():
    pass

def Delete_contact():
    pass


def main():
    while True:
        print("\n------CONTACT BOOK------")
        print("1. Add Contact.")
        print("2. View Contact.")
        print("3. Search Contact.")
        print("4. Exit.")
        operation_value = select_operation()
        if operation_value == 1:
            add_contact()
        elif operation_value == 2:
            content = view_contact()
            print(content)
        elif operation_value == 3:
            Search_contact()
        elif operation_value == 4:
            break

main()