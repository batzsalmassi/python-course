# Write a Python program that takes a user's name as input and prints a greeting message using the input.
name = input("Enter your name: ")
print("Hello there " + name + "!")

# Create a program that takes a sentence as input and prints it in uppercase.
sentence = "This is a sentence."
print(sentence.upper())

# Write a Python script that takes a string as input and prints its length.
string = input("Enter a sentence: ")
print(len(string))

# Write a Python program that takes a sentence as input and prints every second word in reverse order.
##### ------- First Way ------- #####
sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)
for i in range(1, len(words), 2):
    print(words[i][::-1])

##### ------- Second Way ------- #####
words = input("Enter a sentence: ").split()
for word in words[1::2]:
    print(word[::-1])

#Write a Python program that takes ip address in this format : xxx.xxx.xxxx.xxx/xx and print the subnet mask and the ip in separate lines
ip = input("Enter IP address in this format: xxx.xxx.xxx.xxx/xx: ")
ip_address, subnet_mask = ip.split("/")
print("IP Address: " + ip_address + "\n" + "Subnet Mask: " + subnet_mask)

# a good password generator takes the 3 first letters and last 3 letters of the the user full name Example: hothaifa zoubi -> password will be ubihot
full_name = input("Enter your full name: ")
print("The generated password is: " + full_name[:3] + full_name[-3:])
