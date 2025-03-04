def count_digits(num):
    return len(str(abs(num)))

num = int(input("Enter a number: "))
print("Number of digits: ", count_digits(num))