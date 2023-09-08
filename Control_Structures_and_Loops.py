"""
Exercise 1
Write a Python program that prints the first 10 Fibonacci numbers using a loop.
"""

a = 0  # El primer numero de la secuencia es 1
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

# No confiar en el usuario, es bueno implementar manejo de errores
prime = abs(int(input("Type a number to find out if it is a prime number:\n>>> ")))
n  = 2
count = 0
while n <= prime:  # Se puede usar "while n <= (primer ** 0.5) + 1:"
    if prime % n == 0:
        count += 1
    
    if count > 2:
        print(f"The number {prime} does not a prime")
        break

    n  += 1
    if n + 1 == prime:
        print(f"The  number {prime} is prime")
        break


# OBSERVACIONES
# Seguir guia de estilos de codigo python PEP8: Espacios despues de las comas, dos lineas
# vacias antes y despues de definir una funcion, espacio despues de # en los comentarios
#  ... https://peps.python.org/pep-0008/

# Aunque esto resuelve el problema, es aconcejable encapsular la logica del programa en funciones, una
# funcion para obtener entrada del usuario, y otra para realizar la operacion deseada con esta entrada
# del usuario

# Una mejor forma de verificar si un numero es primo


def is_it_prime(number: int) -> bool:
    """
    Check if a given number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
        number (int): The number to be checked for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
