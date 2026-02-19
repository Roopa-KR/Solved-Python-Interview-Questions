# Using list comprehension to create a new list of squares of the numbers if number is even else  cube of number
#Expected output: [144, 125, 343, 324, 27, 100, 15625]
nums = [12, 5, 7, 18, 3, 10, 25]
res = [num ** 2 if num % 2 == 0 else num ** 3 for num in nums]
print(res)