import random



while True:


    n = random.randint(1, 10)



    input("Enter to Start")
    print("---------------------")



    while True:
        x = int(input("Enter number that u think: "))
        if x > n:
            print(f"ur Number {x} is too big")
        if x < n:
            print(f"Ur number {x} is too small")
        if x == n:
            print(f"U won, number was {n}")
            break
    a = input("Enter exit to leave ")
    if a == "exit":
        break