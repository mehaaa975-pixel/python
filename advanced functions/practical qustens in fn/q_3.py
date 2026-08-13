def sum_all(*args):
    total = 0

    for num in args:
        total += num

    return total


print(sum_all(10,20,30))
