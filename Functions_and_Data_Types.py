"""
Exercise 1
Write a Python function called find_maximum that takes a list of numbers as input
and returns the maximum number from the list.
"""
def find_maximun(list):
    list.sort()
    return list[-1]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(find_maximun(list))

"""
Exercise 2
Create a Python function called reverse_string that takes a string as input and returns
the reversed string.
"""
def reverse_string(string):
    return string[::-1]

string = "Lists (known as arrays in other languages)"

print(reverse_string(string))