# sorting a dictionary by keys
dict1={23:"Aron",1:"Alice",5:"Midari"}
dict2={}
n=sorted(dict1.keys())
for i in n:
    dict2[i]=dict1[i]
print(dict2)