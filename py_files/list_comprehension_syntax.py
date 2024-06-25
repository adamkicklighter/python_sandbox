input_string = 'Short example.'
upper_words = [word.upper() for word in input_string] # Wrong temporary variables
print(upper_words)

upper_char = [char.upper() for char in input_string] # Correct temporary variables
print(upper_char)

"""
The temporary variable used does not dictate how the list comprehension operates. Incorrectly substituting `word` instead of `char`
in the examples above does not prevent the operation from returning the correct output. The string method .upper() is what
dictates the operation in the list comprehension.
"""

