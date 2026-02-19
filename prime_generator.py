#prime generator
n=int(input("enter a limit : "))
primes=[x for x in range(1,n)if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)