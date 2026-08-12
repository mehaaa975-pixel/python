def show_details(**keywargs):
    for key,value in keywargs.items():
        print(f"{key}:{value}")


show_details(name="alice",age=20,city="mumbai")
