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

contact_info = "ContactDetails.json"    #assign json file path to contact_info

def select_operation():
    # runs until the right operation is selected
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
    contact_name = input("\n Name: ")

    while True:     #run until the phone number is all in digits
        phone_no = input("Ph_no: ")
        if phone_no.isdigit():
            break
        else:
            print("Ph_No can only be digits.")
    
    email = input("Email: ")

    #the data is loaded here so the old data don't get deleted when we dumps the new data into json file
    try:
        with open(contact_info, "r") as file:       #open the json file in read only operation
            data = json.load(file)                  #loads all the data of the json into data

    #catch these two errors in case if the json file don't exsits and create the data dictionary
    except (FileNotFoundError, json.JSONDecodeError):   
        data = {
            "name" : [],
            "phone" : [],
            "email" : []
        }

    #append the data into the data dictionary
    data["name"].append(contact_name)  
    data["phone"].append(phone_no)
    data["email"].append(email)

    # here we are opening the json file in write-only mode, that let us update the json data
    with open(contact_info,"w") as file:
        json.dump(data, file, indent=4) #dumps the new data into the json file through file (which is in write mode) and leave 4 extra spaces

    print("Successfully Saved.")
        


def view_contact():
    #here we are opening/loading the entire data of the json file, it's in read-only mood meaning we can't edit the data
    # exception handling is used so if the json file is empty or don't exist's it will return NO Contact inseated of error
    try:
        with open(contact_info, "r") as file:
            return json.load(file)
    except:
        return "No Contect Found."

def Search_contact():
    search_throuth_name = input("Enter the name: ")

    #the json file is loaded here so we can find the desire contect if it exists
    with open(contact_info,"r") as info_retrive:
        data = json.load(info_retrive)

        for i in range(len(data["name"])):
            if search_throuth_name == data["name"][i]:
                print(f"\nName: {data["name"][i]} Phone: {data["phone"][i]} Email: {data["email"][i]}")
                break
        else:
            print("\nContact Don't Exist.")


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
            for i in range(len(content['name'])):
                print(f"{i+1}. Name: {content['name'][i]} Ph_No: {content['phone'][i]} Email: {content['email'][i]}")
        elif operation_value == 3:
            Search_contact()
        elif operation_value == 4:
            break


main()