try:
    number = int(input("Enter a number: "))
    print("Square:", number ** 2)

except ValueError:
    print("Invalid number entered.")

else:
    print("Calculation successful.")

    finally:
    print("Execution completed.")