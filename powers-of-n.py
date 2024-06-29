print("Program to print the powers of x raised to N times")

n = int(input("Enter N: "))
x = int(input("Enter x: "))

for i in range(1, n):
	print(f"{x} raised to {i} is {x**i}")