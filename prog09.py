# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

print("Even numbers from 0 to 100:")

for num in range(0, 101):

    if num % 2 == 0:
        print(num, end=" ")