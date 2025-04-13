def prime(num):
    if num <= 1:
        print("Number is not prime")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("The number is not prime")
                break
            else:
                print("The number is prime number")

num = int(input())
print(prime(num))