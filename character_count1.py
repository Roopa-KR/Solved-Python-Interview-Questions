s="qqqqqqqqqdddddddkkkkkkkaaksjdfgn"
d={}
for ch in s:
    if ch in d.keys():
        d[ch]+=1
    else:
        d[ch]=1
for k,v in d.items():
    print(f"{k}:{v}",end=" ")
