row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
i=0
while i<row:
    j=0
    while j<col:
        if i==0 or i==row-1 or j==0 or j==col-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1