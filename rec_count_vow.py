def countv(s):
    vow="aeiouAEIOU"
    if len(s)==0:
        return 0
    elif s[0] in vow:
          return 1 + countv(s[1:])
    else:
        return countv(s[1:])
s="vowel"
countv(s)