number = int(input("Enter a number: "))
k = number
min_digit = number % 10
while number > 0:
    dig = number % 10
    if dig < min_digit:
        min_digit = dig
    number = number // 10

print(f"The smallest digit in {k} is {min_digit}")


# number = input("Enter a number: ")
# min_digit = min(number)
# print(f"The smallest digit in {number} is {min_digit}.")
