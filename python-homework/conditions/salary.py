salary = int(input("Enter your salary: ")) # input the salary
if salary > 14000: # check if the salary is greater than 14000
    print(f"{'Salary after taxes '}{salary * 0.66}") # print the salary after taxes
else: # if the salary is less than 14000
    print(f"{'Salary after taxes '}{salary * 0.87}") # print the salary after lower taxes


num1 = input("Enter a number: ") # input a number
num2 = input("Enter another number: ") # input another number
if num1 > num2: # check if the first number is greater than the second number
    print(f"{'The greater number is '}{num1}") # print the first number
elif num1 == num2: # check if the first number is equal to the second number
    print(f"{'The numbers are equal'}") # print that the numbers are equal
else: # if the first number is less than the second number
    print(f"{'The greater number is '}{num2}") # print the second number