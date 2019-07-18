"""Write a program (function!) that takes a list and
returns a new list that contains all the elements of the first list minus all the duplicates."""

def rmvDuplicates(usr_list):
    return list(set(usr_list))

usr_list=[1,1,1,2,3,4,5,5,5,6,7,7,8]
print("The original list containing duplicates is : " + str(usr_list))
print("The new list containing unique elements is : " + str(rmvDuplicates(usr_list)))