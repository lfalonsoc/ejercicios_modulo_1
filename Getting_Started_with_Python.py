"""
Ejercicio 1.
Write a Python program that takes two numbers as input from the user and prints
their sum.
"""
print("Welcome to add progam. Please write two numbers to see the result")
# Captura de datos
num1 = int(input("Write a first number:\n>>> "))
num2 = int(input("Write the second number:\n>>> "))

print("The add of numbers {} + {} = {}".format(num1, num2, num1 + num2))


""""
Ejercicio 2.
Create a Python program that converts a temperature from Fahrenheit to Celsius.
The user should enter the temperature in Fahrenheit, and the program should print
the equivalent temperature in Celsius.
"""
print("Welcome to program to convert Fahrenheit to Celcius temparature")
# Capture de Fahrenheit temperature
fahrenheit = float(input("Write a Fahrenheit temperature value:\n>>> "))

print(f"The temperature of {fahrenheit} °F in Celcius is {round((fahrenheit -32) * 5 / 9, 2)} °C")