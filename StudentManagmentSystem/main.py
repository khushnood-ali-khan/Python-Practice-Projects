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
#       Count how many students got each grade (A+, A, B, etc.).
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
                        "Roll No": 1,
                        "Name": "",
                        "Age" : 0,
                        "Marks" : [],
                        "percentage" : 0,
                        "Grade" : ""
                    }
                    print(f"\n *--- {i+1} Student Entry ---*")

                    #       Name
                    name = input("Student Name: ")
                    student["Name"] = name                 #assign the name into the dictionary

                    #       Roll NO
                    while True:         #checks if the roll no is valid and don't exists already
                        roll_no = input("Roll No: ").strip()
                        if roll_no.isdigit():
                            roll_no = int(roll_no)
                            for check_roll_no in data:
                                if check_roll_no["Roll No"] == roll_no: print("Roll No Exists!")
                                else:
                                    if roll_no < 1: print("Roll NO can't be less then 1!") ; break
                                    else: student["Roll No"] = roll_no ; break     #assign roll no into the dictionary
                            else: student["Roll No"] = roll_no ; break      #runs when the json file/data is empty
                            break
                        else: print("Invalid Roll NO!")
                    
                    #       AGE
                    while True:
                        age = input("Age: ").strip()
                        if age.isdigit(): age = int(age) ; student["Age"] = age ; break    #assign age into the dictionary
                        else: print("Invalid Age!")
                    
                    #   Marks
                    for k in range(5):       #runs for taking 5 subjects marks
                        while True:          #checks if the marks are the right type
                            marks = input(f"Marks in subject {k+1}: ").strip()
                            if marks.isdigit(): marks = int(marks) ; student["Marks"].append(marks)  ; break      #assign marks to dictionary
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
            sorted_by_rollno = sorted(records, key=lambda x: x["Roll No"])       #using lambda to sort the data by rollno
            for i in sorted_by_rollno:
                print(f"Roll No: {i['Roll No']} Name: {i['Name']} Age: {i['Age']} Marks: {i['Marks']} Percentage: {i['percentage']:.2f} Grade: {i['Grade']}")
    except(FileNotFoundError, json.JSONDecodeError):
        print("There isn't any records!")

def searchstudent():
    Grading()
    print("-----Select Your Option-----")
    print("1. Search by Name")
    print("2. Search by RollNo")
    while True:
        option = input("Select Either 1 or 2: ").strip()
        if option.isdigit():
            option = int(option)
            if option == 2:
                while True:
                    rollno_search = input("Student Roll NO: ").strip()
                    if rollno_search.isdigit():
                        rollno_search = int(rollno_search)
                        try:
                            with open(RECORDS, "r") as f:
                                file = json.load(f)
                            for rollno_search in file: print(rollno_search) ; return
                            else: print("Student Not Found!")
                        except(FileNotFoundError, json.JSONDecodeError):
                            print("Empty Record!")

                    else: print("Invalid RollNo!")

            elif option == 1:
                name_search = input("Student Name: ")
                try:
                    with open(RECORDS, "r") as f:
                        file = json.load(f)
                    for name_search in file: print(name_search) ; return
                    else: print("Student Not Found!")
                except(FileNotFoundError, json.JSONDecodeError):
                    print("Empty Record!")

            else: print("Invalid Option!")
        else: print("Invalid Selection!")

def updatemarks():
    marksupdate = input("Enter RollNo to Update Marks: ").strip()
    if marksupdate.isdigit():
        marksupdate = int(marksupdate)
        try:
            with open(RECORDS, "r") as file:
                data = json.load(file)
                new_marks = []
                rollno = marksupdate
                for marksupdate in data:
                    if marksupdate["Roll No"] == rollno:
                        for i in range(5):
                            updated_marks = int(input(f"New Marks for Subject {i+1}: "))
                            new_marks.append(updated_marks)

                        marksupdate["Marks"] = new_marks
                        with open(RECORDS, "w") as f:
                            json.dump(data, f, indent=2)
                        print("Successfully Updated!")
                else: print("RollNo Not Found!")
        except(FileNotFoundError, json.JSONDecodeError):
            print("No Records!")

    else: print("Invalid Input!")

def deletestudent():
    roll_no = int(input("Roll No of the Student: ").strip())
    try:
        with open(RECORDS, "r") as file:
            data = json.load(file)
            for student in data:
                if roll_no == student['Roll No']:
                    data.remove(student)
                    print("Delete Successful!")
                    break
            else: print("RollNo don't exist!")
            with open(RECORDS, "w") as f:
                json.dump(data, f, indent=2)
    except(FileNotFoundError, json.JSONDecodeError):
        print("Empty Record!")

def showtopper():
    topperList = []
    with open(RECORDS, "r") as file:
        data = json.load(file)
        for per in data: topperList.append(per['percentage'])
        topper = max(topperList)
        for student in data: 
            if student["percentage"] == topper:
                print(f"{student}")

def showclassaverage():
    try:
        with open(RECORDS, "r") as file:
            data = json.load(file)
        count = 0
        total_percentage = 0.0
        for i in data:
            total_percentage += i['percentage']
            count += 1

        average = total_percentage/count

        print(f"Class Average = {average:.2f}")
    except(FileNotFoundError, json.JSONDecodeError):
        print("No Record!")

def saveasCSV():
    try:    #Loads the json data sort them by rollno through lambda and save it as csv
        with open(RECORDS, "r") as file:
            data = json.load(file)
            sorted_data = sorted(data, key=lambda x: x["Roll No"])
            pandasDataframe = pd.DataFrame(sorted_data)
            pandasDataframe.to_csv("Student_Data.csv")
            print("Saved Successfully!")
    except(FileNotFoundError, json.JSONDecodeError):
        print("No Record!")

def percentage_calculation():
    try:
        with open(RECORDS,"r") as file:
            records = json.load(file)
            total_marks = 500
            for data in records:
                if data["Marks"]:
                    obtain_marks = 0
                    for i in range(len(data["Marks"])):
                        obtain_marks += data["Marks"][i]

                data["percentage"] = ((obtain_marks/total_marks) * 100)

        with open(RECORDS, "w") as f:
            json.dump(records, f, indent= 2)

    except(FileNotFoundError, json.JSONDecodeError):
        return

def Grading():
    with open(RECORDS, "r") as file:
        data = json.load(file)
        for grades in data:
            percentage = grades['percentage']
            if percentage >= 90:
                grades['Grade'] = "A+"
            elif percentage >= 80:
                grades['Grade'] = "A"
            elif percentage >= 70:
                grades['Grade'] = "B"
            elif percentage >= 60:
                grades['Grade'] = "C"
            elif percentage >= 50:
                grades['Grade'] = "D"
            else:
                grades['Grade'] = "Fail!"

    with open(RECORDS, "w") as f:
        json.dump(data, f, indent=2)

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
            percentage_calculation()
            Grading()
        elif selected_action == 2:
            viewstudents()
        elif selected_action == 3:
            searchstudent()
        elif selected_action == 4:
            updatemarks()
            percentage_calculation()
            Grading()
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