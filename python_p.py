# Study Demo 
A = 1
B = 2 
print(A + B)
# string 
from string import digits
print("The digits are", digits)
# math
from math import e
print("The value of e is", e)

# notation
message1 = "what's wrong with me"
message2 = 'He said, What did you do?'
print(message1)
print(message2)

# escape Characters
print("He said, \"What's wrong with me?\" to the girl.")

print("This will\nbe on two lines.")

print("\tThis will\thave some\tgaps.")

# Numbers and String
print(1 + 2)
print("1" + "2")

# String equality
print("Dog" == "Dog")
# String inequality
print("Dog" != "Cat")
# String ordering
print("Aardvark" < "Zoo")
print("Orange" >= "Apple")

# membership in string 
# String membership
print("house" in "boathouse")
print("cow" in "cowabunga")
print("y" not in "axes")
print("xe" not in "axes")

# All strings contain the empty string
print("" in "all strings contain the empty string")

# Spaces are characters too
print(" " in "this string contains a space character")

# You can use variables containing string values too
word = "apple"
print(word in "applesauce")
print("p" in word)
print("w" not in word)

person_name = "Grace Hopper"
print(person_name[5])  # Prints the space character!