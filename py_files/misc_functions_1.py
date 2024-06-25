"""
Returning a value without a print statement requires a subsequent print call with the function.

Invoking a function with a print statement in the return does not require a subsequent print call.

If one were to use a print function when invoking a function that already returns a printed value, it prints twice.
"""


# Subsequent print function
def my_func_1(text):

    return 'zzz'

sen = "This sample sentence."

print(my_func_1(sen))

# Print function integrated into the function call
def my_func_2(text):

    return print('zzz')

my_func_2(sen)

# Illustrating the duplicative print by calling a second print function outside of the declared function
print(my_func_2(sen))