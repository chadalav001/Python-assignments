
example = (1,'hello',3,'world',5,8,5,9,'venkat')
example_1 = example.index(3)
example_2 = example.count(5)
example_3 = example + ("sai" ,)
example_4 = list(example)
example_4.remove(3)
example = tuple(example_4)
print(f"The index of a 3rd element  is {example[2]}")
print(f"The Last three elements of this tuple are {example[-3::]}")
print(f"The index of a particular element  is {example_1}")
print(f"This particular element is repeated {example_2} times")
print(f"Here is the added element to out tuple {example_3}")
print(example)
