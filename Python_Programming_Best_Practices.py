"""
Exercise 1
Write a Python function called is_palindrome that checks if a given word is a
palindrome. The function should have proper error handling and be tested with
unittest.
"""
def is_palindrome(word):
    return word == word[::-1]

word = 'malayalam'

result = is_palindrome(word)

if result:
    print("The word {} is a palindrome!".format(word))
else:
    print("The word {} is not a palindrome!".format(word))

"""
Exercise 2
Create a Python decorator called timer that measures the time taken to execute a
function. Use this decorator on a function that sorts a list of random numbers and
prints the sorted list.
"""
import time, random

def funcion_timer(funcion_b):
    def funcion_dec(*args, **kwargs):
        time_start = time.time()
        result = funcion_b(*args, **kwargs)
        time_final = time.time()
        execute_time = time_final - time_start

        return result, execute_time

    return funcion_dec

@funcion_timer
def sorter_list(list):
    list.sort()
    return list

list_number = []
for x in range(10):
    list_number.append(random.randint(0, 100))

answer = sorter_list(list_number)
print(f"List to be sorted {list_number}")
print(f"Sorter list {answer[0]}")
print("Execution time: {} s".format(answer[1]))
