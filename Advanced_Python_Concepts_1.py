""""
Exercise 1
Write a Python class called BankAccount with methods for depositing, withdrawing,
and checking the account balance.
"""
import os, platform

_system = platform.system()
if _system == 'Windows':
    clean_window = 'cls'
else:
    clean_window = 'clear'


class BankAccount:
    def __init__(self, initial):
        self.balance = initial

    def depositing(self, value_int):
        self.balance = self.balance + value_int
        return self.balance

    def withdrawing(self, value_out):
        # Es importante verificar si el balance no sera negativo despues de la transaccion
        self.balance = self.balance - value_out
        return self.balance

    def account_balance(self):
        return self.balance


def get_values(prompt, _type):
    while True:
        value = input(prompt)
        try:
            if int(value) == 0:
                # Si el usuario quiere ingresar una cantidad de dinero entre 0 y 0.9, no va a funcionar
                # en cambio se le va a limpiar la pantalla
                return int(value)
            elif _type(value) > 0:
                return _type(value)
            else:
                input("The value must be greater than 0!")
        except ValueError:
            input("The value must be a number!")
            os.system(clean_window)

def get_input(prompt, options, _type):
    while True:
        try:
            value = input(prompt)
            if _type(value) in options:
                return _type(value)
            else:
                input("Incorrect input!!!")
                os.system(clean_window)
        except ValueError:
            input("Please select one of the options")
            os.system(clean_window)

options = [1, 2, 3, 4]
option = -1
while option != 4:
    if option == -1:
        print("To open your account enter the value to get started")
        initial = get_values("Please enter a value or enter cero (0) to exit the application:\n>>> ", float)
        if initial == 0:
            os.system(clean_window)
            break
        else:
            account = BankAccount(initial)
            input(f"You have opened an acount with ${account.balance}")
            os.system(clean_window)
            option = 0
            continue

    if option >= 0:
        text = "Select an option:\n"
        text += "1. Depositing\n"
        text += "2. Withdrawing\n"
        text += "3. Checking Balance\n"
        text += "4. Exit the application\n>>> "
        option = get_input(text, options, int)
        os.system(clean_window)

        if option == 1:
            print("Deposit money to your account")
            deposit = get_values("Please enter a value:\n>>> ", float)
            account.depositing(deposit)
            input(f"You have depositing ${deposit}!")
            os.system(clean_window)
            option = 0
        elif option == 2:
            print("Withdrawing money to your account")
            withdrawing = get_values("Please enter a value:\n>>> ", float)
            account.withdrawing(withdrawing)
            input(f"You have withdrawing ${withdrawing}!")
            os.system(clean_window)
            option = 0
        elif option == 3:
            balance = account.account_balance()
            os.system(clean_window)
            input(f"Your balance actally is: ${balance}")
            os.system(clean_window)
            option = 0

print("Thank you for visiting the application.\nWe look forward to seeing you soon.")


# OBSERVACIONES
# Seguir guia de estilos de codigo python PEP8: Espacios despues de las comas, dos lineas
# vacias antes y despues de definir una funcion, espacio despues de # en los comentarios
#  ... https://peps.python.org/pep-0008/

# Seria bueno tener bien documentado el codigo, con anotaciones de tipo, docstring, comentarios, ...
