movies = ["lior", "david", "7", 6, 8, 5, "avi", 8]

for i in movies:
    # Check if 'i' is a string and consists only of alphabetic characters
    # isinstance is used to check if 'i' is an instance of the specified type (str in this case)
    # isalpha is used to check if 'i' consists only of alphabetic characters
    if i == "avi":
        i.title()
        break
    elif (type(i)) != str:
        continue
    elif i.isalpha():
        print(i.title())
    else:
        continue
