from itertools import product, permutations
a = {1, 2}
letters=("A", "B", "C")
print(list(product(range(3), letters)))
print(list(permutations(letters)))
print(list(product(range(3), a)))
print(len(list(product(range(3), a))))