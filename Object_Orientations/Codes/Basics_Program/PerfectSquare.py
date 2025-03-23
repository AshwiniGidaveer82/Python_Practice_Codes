number = int(input("Enter a number: "))
if (number ** 0.5).is_integer():
    print(f"{number} is a perfect square number")
else:
    print(f"{number} is not a perfect square number")