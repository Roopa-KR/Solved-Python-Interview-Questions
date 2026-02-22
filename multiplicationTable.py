def multiplicationTable(N):
    for i in range(1,11):
        print(f"{N} x {i} = {N*i}")

N=int(input("N = "))
multiplicationTable(N)