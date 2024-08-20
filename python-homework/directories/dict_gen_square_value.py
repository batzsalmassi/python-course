#write a script that gets a num from the user, if the num is less than 0 ask for a new num
#if the num is greater than 0 it creates a dictionary with the keys of the number
#and the value is the square index of the key
#The script should print the dictionary
#The script should continue to ask the user to enter the num until a positive num is entered

import random
num = int(input("Enter a number: "))
dict = {}
while num < 0:
    num = int(input("Enter a positive number: "))
for i in range(1, num+1):
    dict[i] = i**2
print(dict)

# dict = {k: k**2 for k in range(num)} - This is a more concise way to create the dictionary.
#using for loop in the dictionary comprehension to create the dictionary with the keys and values.

