"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list
of only the first and last elements of the given list. For practice, write this code inside a function."""

def usrdef_List(inp_list):
    fnl_list=[]
    fnl_list.append(inp_list[0])
    fnl_list.append(inp_list[len(inp_list)-1])
    return fnl_list

a = [5, 10, 15, 20, 25]
print(usrdef_List(a))