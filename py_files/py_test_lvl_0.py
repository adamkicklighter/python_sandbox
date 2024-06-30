# [0]

"""
Write a Python function called `is_even` that takes an integer as input and returns `True` if the number is even and `False` otherwise.
"""

# Given

def is_even(number):

    return number % 2 == 0

# Test cases
# print(is_even(4))  # Output: True
# print(is_even(7))  # Output: False


"""
Write a python function called `sum_of_list` that takes a list of numbers as input and returns the sum of all the numbers in the list.
"""

# Given

def sum_of_list(numbers):

    return sum(numbers)

# print(sum_of_list([1, 2, 3, 4]))  # Output: 10
# print(sum_of_list([10, -2, 5]))   # Output: 13


"""
Write a Python function called `reverse_string` that takes a string as input and returns the string reversed.
"""

# Given

def reverse_string(text):

    return text[::-1]

print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python")) # Output: "nohtyP"