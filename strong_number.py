s=list(map(int, input("try 145 :")))
l=[]
def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)
for i in s:
    l.append(fact(i))
print(sum(l))
    