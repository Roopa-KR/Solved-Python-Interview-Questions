def check_pal(s):
    if len(s)==0:
        return True
    elif s[0]==s[-1]:
        return check_pal(s[1:-1])
    else:
        return False
s=input("Enter a string: ")
check_pal(s)