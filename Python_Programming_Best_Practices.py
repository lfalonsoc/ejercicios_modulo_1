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