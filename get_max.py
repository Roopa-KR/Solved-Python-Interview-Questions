#  find the maximum occurring character in a string
#used get method of dictionary to find the maximum occurring character in a string
s="iiiddddhhhsii"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxim=max(d,key=d.get)
print(maxim)