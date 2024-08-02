x = int(input("Enter a number: "))
thausands = (x % 10000) // 1000
hundrends = (x % 1000) // 100
tens = (x % 100) // 10
units = x % 10
print(f"{'Thausands :'} {thausands}\n{'Hundrends :'} {hundrends}\n{'Tens :'} {tens}\n{'Units :'} {units}")