import numpy as np
arr=np.array([1,5,3,4])
max_arr=0
for i in arr:
    if max_arr<i:
        max_arr=i
print(max_arr)
