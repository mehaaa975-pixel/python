def outer():
    def inner():
        print("inner function called")
    print("outer function called")
    inner()

outer()