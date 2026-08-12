def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func


add = outer_func(5)
print(add(10))