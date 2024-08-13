height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight / (height ** 2)) # BMI = weight / height^2
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif 18.5 <= bmi < 25: # 18.5 <= bmi < 25 is equivalent to 18.5 <= bmi and bmi < 25
    print(f"Your BMI is {bmi} and you are normal weight.")
elif 25 <= bmi < 30: 
    print(f"Your BMI is {bmi} and you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")

