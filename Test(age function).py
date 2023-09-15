def age(name, birthdate):
	year = 2023
	print("hello, " + name + " ur age is: ")
	return year - birthdate
	
birthdate = int(input("enter ur birth year: "))
name = str(input("enter ur name: "))
print(age(name, birthdate))