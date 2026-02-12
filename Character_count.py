#input : "a,b,c,a,b,c,a,b,c,a,b"
#expected output : a:4 b:6 c:3
lst1="a,b,c,a,b,c,a,b,c,a,b"
lst2=lst1.split(",")
visited=[]
for char in lst2:
    if char  not in visited:
        visited.append(char) # Adding unique values to variable visit
        print(f"{char}:{lst2.count(ch)}",end="  ") 
