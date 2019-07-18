"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,21,21]

len_ListA = len(a)
len_ListB = len(b)
comm_list = []

if len_ListA > len_ListB:
    for x in a:
        if x in b:
            comm_list.append(x)
else:
    for x in b:
        if x in a:
            comm_list.append(x)

print(str(set(comm_list)))
