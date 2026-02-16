
'''
Expected outcome :
* * * * * 
* 1 2 3 * 
* 1 2 3 * 
* 1 2 3 * 
* * * * * 
'''
n=int(input("Enter the value of n: "))
for i in range(0,n+1):
    for j in range(0,n+1):
        if i==0 or i==n or j==0 or j==n:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()