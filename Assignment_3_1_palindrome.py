'''Write a Python program that checks if a given string is a palindrome.
A palindrome reads the same backward as forward.'''
#palindrome words ex : civic, radar, level, rotor, kayak, madam, and refer

ex = True
while ex:
    user = input(" Give a word to check is it a palindrome or not: ")
    reverse = user[::-1]
    if  user == reverse:
        print(f"The given word {user} is palindrome ")
    else:
        print(" The given word is not a palindrome")
    stop = input("do you want to stop TYPE YES OR else NO: ").lower()
    if stop == "yes":
        print("Thank you")
        break
