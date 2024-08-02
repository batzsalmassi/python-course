salary = int(input("Enter your salary: ")) # input the salary
if salary > 14000: # check if the salary is greater than 14000
    print(f"{'Salary after taxes '}{salary * 0.66}") # print the salary after taxes
else: # if the salary is less than 14000
    print(f"{'Salary after taxes '}{salary * 0.87}") # print the salary after lower taxes