'''6. Check if a Number is Positive or Negative
Write a Python program that asks the user for a number and checks if it is positive, negative, or zero.'''


while True:
    user = int(input("give me a number to know what is it: "))
    if user >0:
        print(f"The give number {user} is a positive number")
    elif user<0:
        print(f"The given number {user} is a negative number")
    elif user == 0:
        print(f"The given number is Zero")
    exit = input("Do you want to check another number? (yes/no): ").lower()
    if exit != 'yes':
        print("Done Have a good day")
        break