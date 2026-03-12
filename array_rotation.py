#input: 1 2 3 4 5
#       2
#output: 4 5 1 2 3
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def arr_rotation(arr,k):
    n=len(arr)
    k=k%n

    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr
if __name__=="__main__":
    arr=list(map(int,input().split()))
    k=int(input())
    print(arr_rotation(arr,k))