number = input("Enter a number ")
print("Multiplication table for " + str(number) + " is\n")
i = 0
while i <= 10:
	print(str(number) + " * " + str(i) + " = " + str(int(number * i)) + "\n")
	i = i + 1
