num = int(input("Enter a number: "))
n = len(str(num))
temp = num
res = 0;
while (temp > 0):
    digit = temp % 10
    res += digit ** n
    temp = temp // 10
if (res == num):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
