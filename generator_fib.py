#  fibonnaci series using generator
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fib()
n=int(input("enter the rage :"))
for _ in range(n):
    print(next(f))