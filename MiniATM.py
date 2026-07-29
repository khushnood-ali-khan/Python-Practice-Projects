#                Mini ATM ⭐⭐
#    Start with:
#    Balance = 5000

#    Show menu repeatedly.
#        1. Check Balance
#        2. Deposit
#        3. Withdraw
#        4. Exit

# Rules:
#   Cannot withdraw more than balance.
#   Deposit must be positive.
#   Continue until Exit.

balance = 5000
counter = True

def checkBalance(amount):   #Check the Balance
    return amount

def Deposit():          #Deposit the amount
    depositamount = int(input("Enter Deposit Amount: "))
    global balance
    if depositamount < 1:
        return "Enter a Valid Amount"
    return (balance + depositamount)

#Withdraw the amount if the balance is Sufficient
def WithDraw(amount):
    withdrawAmount = int(input("Enter Withdraw Amount: "))
    global balance
    if (amount >= withdrawAmount) and withdrawAmount >= 1:
        balance -= withdrawAmount
        return "Amount WithDraw."
    return "Insufficient Balance"

def Exit():
    pass

while counter:
    print("\n----------WHAT WOULD YOU LIKE TO DO ?-----------\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit\n")

    operation = int(input("Choose your Option: "))

# Checking which operation does the user want
    if operation == 1:
        print(f"The Amount is: {checkBalance(balance)}")

    elif operation == 2:
        amountdeposited = Deposit()
        # balance += amountdeposited
        print(f"New Balance: {amountdeposited} ")

    elif operation == 3:
        WithDrawamount = WithDraw(balance)
        print(WithDrawamount)

    elif operation == 4:
        Exit()
        counter = False
    else:
        print("Invalid Option, Try Again")