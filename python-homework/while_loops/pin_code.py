# create a script that receives a pin code of 3 digits from the user.
#The Correct pin is "321"
#if the pin is incorrect the script should ask the user to enter the pin again and error message should be displayed.
#The script should continue to ask the user to enter the pin until the correct pin is entered and welcome message is displayed

pin = "321" # Define the correct pin code
while True:
    user_pin = input("Enter the correct pin code(3 digits): ") # Get the pin code from the user
    if user_pin == pin: # Compare the user input with the correct pin code
        print("Welcome to the system!") # Display a welcome message if the pin code is correct
        break
    print("Incorrect pin code. Please try again.") # Display an error message if the pin code is incorrect                                                           