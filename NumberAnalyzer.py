#                                                    Number Analyzer ⭐⭐

#     Ask the user for an integer.
#      Tell whether it is:
#       Positive/Negative/Zero
#        Even/Odd
#         Divisible by 5
#          Divisible by both 3 and 7
#           Prime or Not Prime

num = int(input("Enter a Number: "))

def num_(number):   # Function to check Positive, Negative or Zero
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def even_odd(value):    #Check Even or Odd
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"

def divisibleOrNot(value):      #check if divisible by 5
    if value == 0 or value == 1:
        return "Not Divisible by 5"
    elif value % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not Divisible by 5"

def check3and7(value):          #check if divisible by 3 and 7
    if (value % 3 == 0 and value % 7 == 0):
        return "Divisible by 3 & 7"
    else:
        return "Not Divisible by 3 & 7"

def primeOrNot(value):      #chcek if prime or not
    if value <= 1:
        return "Not Prime"
    for i in range(2,value):
        divisibleOrNot = value % i
        if divisibleOrNot == 0:
            return "Not Prime"
        else:
            continue
    else:
        return "Prime"


numbercheck = num_(num)
evenOrodd = even_odd(num)
checkby5 = divisibleOrNot(num)
by3and7 = check3and7(num)
primeOrcomposite = primeOrNot(num)

print("-------The Number is: ---------")
print(numbercheck)
print(evenOrodd)
print(checkby5)
print(by3and7)
print(primeOrcomposite)