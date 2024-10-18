''' Simple Bank Account System
Simulate a simple bank account system. Allow the user to:
Create an account with an initial balance.
View the current balance.
Deposit money.
Withdraw money.
Exit the program. '''

print(" ----WELCOME TO THE BANK----- ")

account = 0

print(" SELECT A OPTION FROM BELOW, \n1 : TO CREATE AN ACCOUNT, \n2: CHECK THE CURRENT BALANCE, \n3: DEPOSIT MONEY, "
      "\n4: WITHDRAW SOME CASH,\n5: EXIT " )

#create
def create(account):
    user.lower=input(" Want to create a account. Press y/N: ")
    if user == "y":
        print("Enter your name: ,\n Enter you ssn: , \n Enter your address: ")
    elif user == "exit":
        print("THANK YOU ")

#current
def current(account):
