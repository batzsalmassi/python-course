# print the prime numbers between 1 and 100 using a for loop
# prime numbers are numbers that are only divisible by 1 and themselves


for i in range(2, 101): # loop through numbers between 1 and 100
    is_prime = True # set the number to be prime
    for j in range(2, i): # loop through numbers between 2 and the number
        if i % j == 0: # if the number is divisible by any number between 2 and the number
            is_prime = False # the number is not prime
            break # break the loop
    if is_prime == True: # if the number is prime
        print(i) # print the number