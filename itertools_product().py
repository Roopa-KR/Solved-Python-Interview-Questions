from itertools import product
A=tuple(map(int,input().split()))

B=tuple(map(int,input().split()))
c=tuple(product(A,B))
print(*c,sep=" ")