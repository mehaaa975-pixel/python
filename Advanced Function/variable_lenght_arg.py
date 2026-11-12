def add_numbers(*args):
    total = 0

    for num in args:
        total = total + num

    print(total)

add_numbers(10, 20, 30, 40)