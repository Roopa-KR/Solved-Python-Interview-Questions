#input : "a,b,c,a,b,c,a,b,c,a,b"
#expected output : a:4 b:6 c:3
lst1="a,b,c,a,b,c,a,b,c,a,b"
lst2=lst1.split(",")
visited=[]
for ch in lst2:
    if ch  not in visited:
        visited.append(ch)
        print(f"{ch}:{lst2.count(ch)}",end=" ")