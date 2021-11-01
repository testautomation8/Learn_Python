""" Example of Map - The function map takes a function and an iterable as arguments,
and returns a new iterable with the function applied to each argument. """
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Example - 1

result = list(map(lambda x: x * 5, nums))
print("Map Example")
print("Original list before applying Map : {}".format(nums))
print("List after using Map function : {}".format(result))


# Example -2

def add_five(x):
    return x + 5


result = list(map(add_five, nums))  # 5 gets added to each item of the list
print("Original list before applying Map : {}".format(nums))
print("List after using Map function : {}".format(result))

""" Example of Filter  - The function filter filters an iterable by removing items that 
don't match a predicate (a function that returns a Boolean)."""

# Example - 1


result = list(filter(lambda x: x % 2 == 0, nums))
print("Filter Example")
print("Original list before applying Filter : {}".format(nums))
print("List after using Filter function : {}".format(result))