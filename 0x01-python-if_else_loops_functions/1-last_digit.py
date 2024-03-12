#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig= str(number)
if int(last_dig[-1]) > 5:
    print(f"Last digit of {last_dig} is {last_dig[-1]} and is greater than 5")
elif int(last_dig[-1]) == 0:
    print(f"Last digit of {last_dig} is {last_dig[-1]} and is 0")
elif int(last_dig[-1]) < 6 and int(last_dig[-1]) != 0:
    print(f"Last digit of {last_dig} is {last_dig[-1]} and is less than 6 and not 0")
