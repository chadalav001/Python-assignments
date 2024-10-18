'''Count Vowels:
Write a function that takes a string as input and counts the number of vowels (a, e, i, o, u) in that string.'''

def user(string):
    vowel = ("a,e,i,o,u")
    count = 0
    string = string.lower()
    for i in string:
        if i in vowel:
            count+=1
    return count
user_input = input("Enter a Word : ")
main = user(user_input)
print(f"The given word{user_input} has {main} vowels")
