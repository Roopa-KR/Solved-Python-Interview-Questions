def rem(s, v=""):
    if len(s) == 0:
        return ""
    
    if s[0] in v:
        return rem(s[1:],v)
    else:
        return s[0] + rem(s[1:], v + s[0])
string = "programming"
print(rem(string))