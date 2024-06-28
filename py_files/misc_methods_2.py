from functools import reduce

def combine_reduce_zip_map():
    """
    This function demonstrates the combined use of functools.reduce, zip, and map.
    It performs the following:
    1. Uses zip to pair elements from two lists.
    2. Uses map to sum the paired elements.
    3. Uses reduce to calculate the product of the summed elements.

    Returns:
        int: The product of the summed pairs.
    """

    # Step 1: Create two lists of numbers
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    # Step 2: Use zip to pair elements from both lists
    paired_elements = list(zip(list1, list2))
    print(paired_elements)

    # Step 3: Use map to sum the pair elements
    # The lambda function takes a tuple (x) and returns the sum of its two elements (x[0]=x[1])
    summed_pairs = list(map(lambda x: x[0] + x[1], paired_elements))
    print(summed_pairs)

    # Step 4: Use reduce to calculate the product of the summed pairs
    # The lambda function takes two arguments (x and y) and returns their product (x * y)
    product_of_sums = reduce(lambda x, y: x * y, summed_pairs)

    return product_of_sums

# Execute the function and print the result
result = combine_reduce_zip_map()
print(f"The product of the summed pairs is: {result}")
