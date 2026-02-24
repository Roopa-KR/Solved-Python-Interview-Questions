def rev(s):
    if len(s)==0 or len(s)==1:
        return s
    return s[-1] + rev(s[:-1])
s=input("Enter a string : ")
rev()