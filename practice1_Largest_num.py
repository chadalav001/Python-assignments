'''Simple Calculator (Addition and Subtraction)
Create a Python program that takes two numbers and an operator (+ or -). Perform the corresponding arithmetic operation.'''

print("-----  Simple Calculator  ------")

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
operator = input(" want to ADD (+) or Subtract (-) Enter the symbols: ")
if operator.lower() == "+":
    print(f"the addition of these two numbers is {num1+num2}")
elif operator.lower() == "-" :
    print(f"the subtraction of these two number is {num1 - num2}")
else:
    print("invalid symbol select + or -")