import random

MIN_OPERAND = 1
MAX_OPERAND = 10

n = random.randint(MIN_OPERAND,MAX_OPERAND)

while True:
    x = input("Enter n: ")
    if  x < str(n):
        print("ur number is too small")
    if x > str(n):
        print("ur number is too big")
    if  x == str(n):
        print("U win")
        break

