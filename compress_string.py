#string compression without using in_built functions
s="aaabbca"
res=''
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        res+=str(count)+s[i-1]
        count=1
res+=str(count)+s[i]      
print(res)
#expected output = 3a2b1c1a