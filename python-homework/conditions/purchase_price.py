# The program asks the user to enter the purchase price of a product and then calculates the price after applying a discount. 
# If the purchase price is greater than 5000, the program applies a 20% discount. If the purchase price is between 1000 and 5000, 
# the program applies a 10% discount. If the purchase price is less than 1000, the program does not apply any discount. 
# The program then prints the price after the discount is applied.
purchase_price = float(input("Enter the purchase price: "))
if purchase_price > 5000:
    over = purchase_price * 0.8
elif  purchase_price >= 1000:
    under = purchase_price * 0.9
else:
    no_discount = purchase_price

#print(f"{'The price after discount is '}{over if 'over' in locals() else under if 'under' in locals() else no_discount}")
print(f"The price after 20% discount : {over}\n The price after 10% discount : {under}\n The price without discount : {no_discount}")
