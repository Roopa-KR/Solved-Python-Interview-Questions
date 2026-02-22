N=int(input())
if N<0:
    while N<=0:
        print(N,end=" ")
        N+=1
elif N>0:
    while N>=0:
        print(N,end=" ")
        N-=1
else:
    print("It's already a zero")