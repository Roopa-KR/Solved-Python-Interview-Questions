def modify(lst):
    lst.append(4)
    print("Inner Function:",lst)
my_lst=[1,2,3]
print("Outer function 1:",my_lst) # before calling function
modify(my_lst)
print("Outer function:",my_lst) # after calling function