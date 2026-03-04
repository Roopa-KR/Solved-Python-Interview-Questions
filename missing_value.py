#  find the missing value in a list of n-1 integers in the range of 1 to n
list1=[1,2,3,5,6]
n=len(list1)+1
total_sum=n*(n+1)//2
sum_lst=sum(list1)
print(total_sum-sum_lst)