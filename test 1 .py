#string_manipulation

print("----- WELCOME TO WORD MANIPULATION  -----")
def letter_histogram(words):
    string = ""
    dictionary = {}

    for string in words:
        if string in dictionary:
            dictionary[string] += 1
        else:
            dictionary[string] = 1
    return dictionary

strings = input("enter a word: ")
print(f"The converted string in dict are {letter_histogram(strings)}")