#                               🎓 Student Management System (Console Application)

# Main Menu
# 1 Add Student
# 2 View Students
# 3 Search Student
# 4 Update Marks
# 5 Delete Student
# 6 Show Topper
# 7 Show Class Average
# 8 Exit

# Each student should have:
#   Name
#   Roll Number
#   Age
#   Marks in 5 Subjects

# Store all students in a list.

# When viewing students, display:
#   Name
#   Roll Number
#   Age
#   Total Marks
#   Percentage
#   Grade

# Grade Rules:
#   90+  A+
#   80+  A
#   70+  B
#   60+  C
#   50+  D
#   else Fail

# Bonus Challenges:
#   If you finish early, try adding these features without learning new topics:
#       Prevent duplicate roll numbers.
#       Display students sorted by percentage (implement your own sorting using loops).
#       Search students by name or roll number.
#        Count how many students got each grade (A+, A, B, etc.).
#       Ask for confirmation before deleting a student.

import json
import pandas as pd

RECORDS = "students_records.json"

def select_operation():
    while True:
        select = input("SELECT YOUR OPERATION: ").strip()
        if select.isdigit():
            select = int(select)
            if (select < 1) or (select > 10):
                print("Invalid Operation!")
            else:
                return select
        else:
            print("SELECT OPERATION BY IT'S NUMBER!!")

def addstudent():
    while True:
        no_of_students = input("\nHow many students do you want to add: ").strip()
        if no_of_students.isdigit():
            no_of_students = int(no_of_students)
            if no_of_students > 0:
                try:            #loads the json old data so it won't get deleted with write operation
                    with open(RECORDS,"r") as file:
                        data = json.load(file)
                except(FileNotFoundError, json.JSONDecodeError):
                    data = []

                for i in range(no_of_students):     #collect student data
                    student = {
                        "name":"",
                        "rollno": 0,
                        "age" : 0,
                        "marks" : []
                    }
                    print(f"\n *--- {i+1} Student Entry ---*")

                    #       Name
                    name = input("Student Name: ")
                    student["name"] = name                 #assign the name into the dictionary

                    #       Roll NO
                    while True:         #checks if the roll no is valid
                        roll_no = input("Roll No: ").strip()
                        if roll_no.isdigit():
                            roll_no = int(roll_no)
                            if roll_no < 1: print("Roll NO can't be less then 1!")
                            else: student["rollno"] = roll_no ; break      #assign roll no into the dictionary
                        else: print("Invalid Roll NO!")
                    
                    #       AGE
                    while True:
                        age = input("Age: ").strip()
                        if age.isdigit(): age = int(age) ; student["age"] = age ; break    #assign age into the dictionary
                        else: print("Invalid Age!")
                    
                    #   Marks
                    for k in range(5):       #runs for taking 5 subjects marks
                        while True:          #checks if the marks are the right type
                            marks = input(f"Marks in subject {k+1}: ").strip()
                            if marks.isdigit(): marks = int(marks) ; student["marks"].append(marks)  ; break      #assign marks to dictionary
                            else: print("Marks Can Only be in digits!")

                    data.append(student)    #append the student record into the data list

                with open(RECORDS, "w") as f:       #save/dumps the whole data along with the new data into json
                    json.dump(data, f , indent=2)
                    print("\n Saved Successfully!")
                    break
                    
            else: print("Can't be less then 1.")
        else: print("Invalid Input!")   #runs when the number of students to add is invalid

def viewstudents():
    try:
        with open(RECORDS,"r") as file:
            records = json.load(file)
            sorted_by_rollno = sorted(records, key=lambda x: x["rollno"])       #using lambda to sort the data by rollno
            for i in sorted_by_rollno:
                print(f"Roll No: {i['rollno']} Name: {i['name']} Age: {i['age']} Marks: {i['marks']}")
    except(FileNotFoundError, json.JSONDecodeError):
        print("There isn't any records!")

def searchstudent():
    pass

def updatemarks():
    pass

def deletestudent():
    pass

def showtopper():
    pass

def showclassaverage():
    pass

def saveasCSV():
    print("comming soon!")

def main():
    while True:
        print("\n---------------STUDENTS MANAGMENT SYSTEM---------------\n")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Show Class Average")
        print("8. Save As CSV")
        print("9. Exit\n")
        selected_action = select_operation()

        if selected_action == 1:
            addstudent()
        elif selected_action == 2:
            viewstudents()
        elif selected_action == 3:
            searchstudent()
        elif selected_action == 4:
            updatemarks()
        elif selected_action == 5:
            deletestudent()
        elif selected_action == 6:
            showtopper()
        elif selected_action == 7:
            showclassaverage()
        elif selected_action == 8:
            saveasCSV()
        elif selected_action == 9:
            print("GOOD BYE!")
            break


main()