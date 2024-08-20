# implement the fibonacci sequence using a while loop
# the sequence should have 20 numbers
# the sequence should start with 0 and 1
fibo = [0,1] # the first two numbers in the sequence
index = len(fibo) # the index of the last number in the sequence
while len(fibo) < 20: # loop until the sequence has 20 numbers
    fibo.append(fibo[index-1] + fibo[index-2]) # add the sum of the last two numbers to the sequence
    index += 1 # increment the index by 1
print(fibo) # print the sequence