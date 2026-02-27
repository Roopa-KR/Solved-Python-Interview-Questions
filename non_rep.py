#Find the first non-repeating character in a string.
s='aabbcddaaa'
print(next(ch for ch in s if s.count(ch) == 1))