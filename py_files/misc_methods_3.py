class StringJoiner:
    def __init__(self, inner_separator, outer_separator):
        """
        Initialize the StringJoiner with specified seprators.

        Args:
            - inner_separator (str): The separator to use within each sublist.
            - outer_separator (str): The separator to use between concatenated sublists.
        """
        self.inner_separator = inner_separator
        self.outer_separator = outer_separator

    def concat_and_join(self, list_of_lists):
        """
        Concatenates elements of each sublist into a single string using the inner separator,
        and then concatenates all these strings into a final result using the outer separator.

        Args:
        - list_of_lists (list of list of str): The input list of lists.

        Returns:
        - str: The final concatenated string.
        """
        # Concatenate each sublist into a stingle string
        concatenated_sublists = [self.inner_separator.join(sublist) for sublist in list_of_lists]

        # Concatenate all the sublist stings into a final results
        final_result = self.outer_separator.join(concatenated_sublists)

        return final_result
    
# Example usage
list_of_lists1 = [
    ['apple', 'banana', 'cherry'],
    ['dog', 'elephant', 'fox'],
    ['grape', 'honeydew', 'kiwi']
]

list_of_lists2 = [
    ['red', 'blue', 'green'],
    ['circle', 'square', 'triangle'],
    ['cat', 'dog', 'mouse']
]

# Create an instance of StringJoiner
joiner = StringJoiner(inner_separator=', ', outer_separator=' | ')

# Use the instance to concatenate and join multiple lists of lists
results1 = joiner.concat_and_join(list_of_lists1)
results2 = joiner.concat_and_join(list_of_lists2)

print(results1)
print(results2)