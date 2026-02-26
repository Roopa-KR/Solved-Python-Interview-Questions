def average(arr):
    l=set(arr)
    res=sum(l)/len(l) 
    return res
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)