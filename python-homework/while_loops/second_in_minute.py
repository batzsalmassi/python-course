import datetime
import time

# while loop to print the current time every second
# while datetime.datetime.now().minute < 16:
#     print(datetime.datetime.now().time())

while True: # infinite loop to print the current second of the minute
    if datetime.datetime.now().minute == 27: # if the current minute is 27
        print("The current second of the minute in: " , datetime.datetime.now().second) # print the current second of the minute
        time.sleep(1) # delay the loop for 1 second