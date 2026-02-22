s="nishclassy"
l=[]
l.extend(s)
for i in range(len(l)):
    if i%2!=0:
        print("".join(l[i]),end="")