# קבלו 5 משתנים מהיוזר
# הפכו אותם לליסט אחד, הוסיפו את המספר 78 לסוף הרשימה
#הוסיפו לאינדקס 4 את המספר 95 ותדאגו ששאר האיברים יזוזו ימינה
# תוציאו את האיברים האחרונים של הרשימה
#אחרי כל אחת מהפקודות בצעו הדפסה של הרשימה

# פתרון תרגיל

list1 = []
# קבלו 5 משתנים מהיוזר
list1.append(input("Enter first number: "))
list1.append(input("Enter second number: "))
list1.append(input("Enter the first word: "))
list1.append(input("Enter the second word: "))
list1.append(input("Enter the third word: "))

print(list1)

# הוסיפו את המספר 78 לסוף הרשימה
list1.append(78)
print(list1)

# הוסיפו לאינדקס 4 את המספר 95 ותדאגו ששאר האיברים יזוזו ימינה
list1.insert(3, 95)
print(list1)

# תוציאו את האיברים האחרונים של הרשימה
list1.pop()
list1.pop()
print(list1)