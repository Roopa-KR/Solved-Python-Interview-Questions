def zero_matrix(matrix,n,m):
    row=[0]*n
    col=[0]*m
    # mark rows and collumn which contains 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    # set 0s in marked rows and collumns
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
#usage
mat=[[1,2,3,4],
     [5,1,7,8], 
     [7,8,9,0]]
result=zero_matrix(mat,3,4)
for r in result:
    print(r)