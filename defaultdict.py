
from collections import defaultdict
d=defaultdict(list)
n,m=map(int,input().split())
for i in range(1,n+1):
    word=input().strip()
    d[word].append(i)
words=[]
for w in range(m):
    words.append(input().strip())
for word in words:
    if word in d:
        print(*d[word])
    else:
        print(-1)
    