try:
    num=(input("Enter a number: "))
    print("Square",num**2)

except ValueError:
    print("Please enter a valid number.")

else:
    print("calculation successful.")
    