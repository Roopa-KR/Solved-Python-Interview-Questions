# A strong number is a number whose sum of the factorial of its digits is equal to the original number.
# For example, 145 is a strong number because 1! + 4! + 5! = 145.
# Write a program to check if a given number is a strong number or not.   
s=list(map(int, input("try 145 :")))

l=[]
def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)
for i in s:
    l.append(fact(i))
print(sum(l))
    