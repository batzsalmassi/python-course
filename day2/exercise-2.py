height = input("Enter your height in Meters: ")
weight = input("Enter your weight in Kilograms: ")

bmi = float(weight) / (float(height) ** 2)
print(f"{'Your BMI is : '}{(round(bmi))}")