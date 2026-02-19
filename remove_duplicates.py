# Remove duplicates from a string and print the unique characters in the order they appear in the string.
def remove_dup(s):
    dit={}
    for x in s:
        if x not in dit.keys():
            dit[x]=1
        else:
            dit[x]+=1
    # return dit 
    for k in dit.keys():
        print(f"{k}",end="")

s=input()
remove_dup(s)
