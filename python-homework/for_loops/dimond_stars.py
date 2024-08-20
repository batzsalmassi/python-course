#the program needs to get a number less than 9 and if it's not qeual number print a dimond of stars
#if the number is 7 it should look like this
#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *

# n = int(input("Enter not equal number lower than 9: "))
# if n >= 9 or n % 2 == 0:
#         print("Number must be less than 9 and odd.")

# # Print the upper half of the diamond
# for i in range(n // 2 + 1):
#     print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

# # Print the lower half of the diamond
# for i in range(n // 2 - 1, -1, -1):
#     print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
        

numbers = int(input("Enter not equal number lower than 9: "))
if numbers >= 9 or numbers % 2 == 0:
        print("Number must be less than 9 and odd.")

# Print the upper half of the diamond
for i in range(1, numbers+1, 2):
    n = (numbers - i) // 2
    print(' ' * n + '*' * i + ' ' * n)

# Print the lower half of the diamond
for i in range(numbers-2, 0, -2):
    n = (numbers - i) // 2
    print(' ' * n + '*' * i + ' ' * n)