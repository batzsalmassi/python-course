# #1.
# num = 100 % 7
# print(num)

# # 2. 
# num = (100 // 7)
# print(num)

# # 3.
# num = int(input("Enter a number: "))
# modulu = num % 3
# print(f"{'Modulu of'} {num} {'is'} {modulu}")
# div = num / 3
# print(f"{'Division of'} {num} {'by 3 is'} {div}")

# # 4.
# num = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# modulu = num % num2 # modulu calculation between 2 numbers
# div = num / num2 # division calculation between 2 numbers
# print(f"{'Modulu of'} {num} {'by'} {num2} {'is'} {modulu}")
# print(f"{'Division of'} {num} {'by'} {num2} {'is'} {div}")

# # 5.
# num = int(input("Enter a number: "))
# # units calculation = num % 10
# # tens calculation = (num % 100) // 10
# # hundrends calculation = (num % 1000) // 100
# # thausands calculation = (num % 10000) // 1000
# print(f"{'Thausands :'} {(num % 10000) // 1000}\n{'Hundrends :'} {(num % 1000) // 100}\n{'Tens :'} {(num % 100) // 10}\n{'Units :'} {num % 10}")

# # 6.
# adress = input("Enter your adress in the following format(house number/building number/street name ): ") #input the address in the mentioned format
# address = adress.split("/") # split the input by "/" and store the result in a list
# print(f"{'House number :'} {address[0]}\n{'Building number :'} {address[1]}\n{'Street name :'} {address[2]}") # print the list of elements

# #  7.

# address = str(input("Enter your address :"))
# address = address.upper()
# address = address.split(",")
# print(f"{'Address:'} {address[0]}\n{'Building Num:'} {address[-1]}")

# 8.
# num = input("Please enter: abc abc abc lior: ".strip())
# change = input("Please enter the word you want to replace: ")
# print(num.count(change)) 
# #print(num.replace(change, "abcd", count-1))


print("       Hello World         ".strip().replace(" ", "abcd")) # remove spaces from the beginning and the end of the string and replace the spaces with "abcd"
print("       Hello World         ".replace(" ", ""))

import math
math

# print("      hello        ".strip()) # remove spaces from the beginning and the end of the string
# print("      hello        ".lstrip()) # remove spaces from the beginning of the string
# print("      hello        ".rstrip()) # remove spaces from the end of the string

# print ("      Hello World     ".index('o')) # return the index of the first occurance of the letter 'o'
# print ("      Hello World     ".rindex('o')) # return the index of the last occurance of the letter 'o'

# print ("      Hello World     ".find('a')) # return the index of the first occurance of the letter 'o'
# print ("      Hello World     ".rfind('a')) # return the index of the last occurance of the letter 'o'