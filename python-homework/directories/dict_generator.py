#write a program that generates a random dictionery with a given length and a given range of values
import random

length = int(input("Enter the length of the dictionary: "))
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

random_dict = {i: random.randint(min_value, max_value) for i in range(length)}

print(random_dict)


