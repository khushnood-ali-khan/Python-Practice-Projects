#                            Library Management (Basic) ⭐⭐⭐⭐
# Books list:
# Python
# Java
# C++
# HTML
# SQL

# Menu:
# 1 View Books
# 2 Borrow Book
# 3 Return Book
# 4 Exit

# Rules:
# Borrow removes from list.
# Return adds back.
# Cannot borrow unavailable books.
# Cannot return duplicates.

import json
shelfs_of_books = "BooksRecords.json"

def operation():
    action = input("\nSELECT YOUR ACTION: ").strip()
    if action.isdigit():
        action = int(action)
        if action < 5:
            return action
        else:
            print("Invalid Opreation!")
    else:
        print("Select the right action by it's number.")

def view_books():
    #checks if there are any books then print them
    try:
        with open(shelfs_of_books,"r") as file:
            books = json.load(file)
        for i in range(len(books)):
            print(f"Book {i+1}: {books[i]}")
    except:
        print("Shelfs are empty.")

def borrow_book():
    try:
        with open(shelfs_of_books,"r") as file:
            books = json.load(file)
        for i in range(len(books)):
            print(f"Book {i+1}: {books[i]}")
    except:
        print("Shelfs are empty can't borrow any book.")
        return

    while True:
        borrowing_book = input("SELECT YOUR BOOK: ").strip()

        if borrowing_book in books:
            books.remove(borrowing_book)
            with open(shelfs_of_books,"w") as f:
                json.dump(books, f, indent=2)
            print("Borrowed Successfully!")
            return
            
        else:
            print("This book isn't avaliable.")
 

def return_book():
    returning_book = input("Enter the Book you want to return: ")

    with open(shelfs_of_books,"r") as f:
        books = json.load(f)
    # book_exists = any(i in books for i in returning_book)

    if returning_book in books:
        print("The Book already Exists.")

    else:
        books.append(returning_book)
        with open(shelfs_of_books,"w") as file:
            json.dump(books, file, indent=2)
            print("Successfully Returned.")

def main():
    while True:
        print("\n-------MENU---------")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        selected_operation = operation()
        if selected_operation == 1:
            view_books()
        elif selected_operation == 2:
            borrow_book()
        elif selected_operation == 3:
            return_book()
        elif selected_operation == 4:
            print("Good bye!")
            break




main()