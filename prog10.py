# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

print("Numbers from 0 to 100 except those ending with zero:")

for num in range(0, 100):

    if num % 10 != 0:
        print(num, end=" ")