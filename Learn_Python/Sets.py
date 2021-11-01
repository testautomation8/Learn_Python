set_a = {0,1,2,3,4,5,6,7,8}
set_b = {2,4,6,8,10,12,14}

print(set_a | set_b)  # union operator | combines two sets to form a new one containing items in either.
print(set_a & set_b)  # intersection operator & gets items only in both.
print(set_a - set_b)  # difference operator - gets items in the first set but not in the second
print(set_b - set_a)
print(set_a ^ set_b)  # symmetric difference operator ^ gets items in either set, but not both.
