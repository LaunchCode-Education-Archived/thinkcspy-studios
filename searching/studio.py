def contains_n(numbers, n):
    for num in numbers:
        if num == n:
            return True
    return False

# testing with some inputs
example_nums = [1, 2, 3, 2]
print( contains_n(example_nums, 0) )
print( contains_n(example_nums, 1) )
print( contains_n(example_nums, 2) )
print( contains_n(example_nums, 3) )
print( contains_n(example_nums, 4) )
