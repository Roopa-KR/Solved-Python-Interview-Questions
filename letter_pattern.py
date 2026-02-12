
'''expected output
A B C D E
B C D E
c D E
d E
E
'''
n=int(input())
ch=65
for i in range(n,0,-1):
    for j in range(0,i):
        print((chr(ch)),end=" ")
        ch+=1
    ch-=j
    print()