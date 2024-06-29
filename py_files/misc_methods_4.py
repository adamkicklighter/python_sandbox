def split_zip_join(input_list):
    # Split the list into pairs
    pairs = zip(input_list[::2], input_list[1::2]) # `::2` is `start:stop:step`

    # Join the pairs back into a single list
    joined_list = [item for pair in pairs for item in pair]

    return joined_list

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = split_zip_join(input_list)
print(result)
