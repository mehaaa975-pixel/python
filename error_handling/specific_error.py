num = int(input("Enter a number: "))
result = 10 / num
print(result)
expect ValueError:
    print("Enter a valid number.")
expect ZeroDivisionError:
    print("Cannot divide by zero.")