numbers = [1, 2, 3, 4, 5]

scale_and_add = lambda x: x * 2 + 3

results = list(map(scale_and_add, numbers))

print(results)