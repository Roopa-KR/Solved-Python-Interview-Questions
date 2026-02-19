#dictionary comprehension
word="banana"
di={i:word.count(i) for i in word}
print(di)