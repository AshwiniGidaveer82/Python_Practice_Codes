def is_anagram_number(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(is_anagram_number(num1, num2))  # Output: True