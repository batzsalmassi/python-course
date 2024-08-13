# Write a Python program that takes a sentence as input and capitalizes the first letter of the sentence.
word = input("enter a sentence: ") # input a sentence
word = word[0:1].capitalize() + word[1:] # capitalize the first letter of the sentence
print(word)


# Write a Python program that takes a sentence as input and prints every second word in reverse order.
string = "hello how are you I'm Sean"
word2 = input("enter your name: ") # input a sentence
if string.split()[-1] == word2:
    print("The last word is the same")