"""
Exercise 1
Write a Python program that prints the first 10 Fibonacci numbers using a loop.
"""

a = 0
b = 1
for x in range(10):
    print(a)
    a, b = b, a + b


"""
Exercise 2
Create a Python program that checks if a given number is prime or not. The user
should input a number, and the program should print whether it is prime or not.
"""

print("Welcome to program tha knows if the number is a prime")

prime = abs(int(input("Type a number to find out if it is a prime number:\n>>> ")))
n  = 2
count = 0
while n <= prime:
    if prime % n == 0:
        count += 1
    
    if count > 2:
        print(f"The number {prime} does not a prime")
        break

    n  += 1
    if n + 1 == prime:
        print(f"The  number {prime} is prime")
        break
