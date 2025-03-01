# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is bigger.")
else:
    print(f"{num2} is bigger.")