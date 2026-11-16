nums = [1, 2, 3, 4, 5]
saquare  = list(map(lambda x: x**2, nums))
print(saquare)


even_nums = list(filter(lambda x: x%2==0, nums))
print(even_nums)



from functools import reduce
total = reduce(lambda x, y: x+y, nums)
print total