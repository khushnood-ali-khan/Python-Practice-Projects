#       Student Grade Calculator ⭐ (Easy)

name = input("Enter your name: ")
rollno = int(input("Enter your RollNo: "))

sub : list[int] = []
total_marks = 500
i = 1

for i in range(5):
    mark = int(input(f"Enter Subject {i+1} Marks: "))
    sub.append(mark)

def calcu_sum(subjects: list[int]=[]):
    sum = 0
    for k in range(len(subjects)):
        sum += subjects[k]
    return sum

#Calculate percentage
def calcu_percentage(obtain_marks):
    return (obtain_marks/total_marks)*100

# grades Function
def grade(percen):
    if percen >= 90:
        return "A+"
    elif percen >= 80:
        return "A"
    elif percen >= 70:
        return "B"
    elif percen >= 60:
        return "C"
    elif percen >= 50:
        return "D"
    else:
        print("Fail.")


obtain = calcu_sum(sub)
percentage = calcu_percentage(obtain)
student_grades = grade(percentage)

print("*-------Result-------*")
print(f"Name: {name}")
print(f"RollNO: {rollno}")
print(f"Obtain Marks: {obtain} / {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {student_grades}")