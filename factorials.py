def fact(n):
	if n == 1:
		return 1
	return fact(n - 1) * n
	
x = int(input("Please Enter Number: "))

print(fact(x))