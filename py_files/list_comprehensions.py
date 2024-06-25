squares = [x**2 for x in range(1, 11)]
print(squares)

even_squares = [x**2 for x in range(1, 11) if x % 2 ==0] # If x modulo 2 equals zero
print(even_squares)

coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

test = [(x) for x in range (5)]
print(test)

# Flatten a matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
flattened = [num for row in matrix for num in row]
print(flattened)

numbers = [1,2,3,4,5,6,7,8,9,10]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(labels)