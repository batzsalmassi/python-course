# This program checks if a string is a palindrome
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward
#  (ignoring spaces, punctuation, and capitalization).
s = input("Enter a string: ") # Get the string from the user
s = s.replace(" ", "").lower() # Remove spaces and convert to lowercase
if s== s[::-1]: # Check if the string is equal to its reverse 
    print("This is a palindrome") # Print a message if the string is a palindrome
else: # If the string is not a palindrome
    print("This is not a palindrome") # Print a message if the string is not a palindrome