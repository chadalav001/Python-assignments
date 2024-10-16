'''Sum of Numbers Until Zero
Write a program that keeps taking numbers as input and adds them to a sum.
The program should stop when the user inputs 0, and then print the total sum.'''

total = 0

sum = True

while sum:
    numbers = int(input("give a number: "))
    if numbers == 0:
        print("The program has stopped")
        break
    total += numbers
    print(f"The total sum is {total}")

