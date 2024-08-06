# קבלו 5 משתנים מהיוזר
# הפכו אותם לליסט אחד, הוסיפו את המספר 78 לסוף הרשימה
#הוסיפו לאינדקס 4 את המספר 95 ותדאגו ששאר האיברים יזוזו ימינה
# תוציאו את האיברים האחרונים של הרשימה
#אחרי כל אחת מהפקודות בצעו הדפסה של הרשימה

# פתרון תרגיל

# קבלו 5 משתנים מהיוזר
var1 = input("Enter first number: ")
var2 = input("Enter second number: ")
var3 = input("Enter the first word: ")
var4 = input("Enter the second word: ")
var5 = input("Enter the third word: ")

# הפכו אותם לליסט אחד
list1 = [var1, var2, var3, var4, var5]
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