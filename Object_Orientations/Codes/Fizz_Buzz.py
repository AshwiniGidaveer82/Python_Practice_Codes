def fizzBuzz(n: int):
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else 
        "Fizz" if i % 3 == 0 else 
        "Buzz" if i % 5 == 0 else 
        str(i) 
        for i in range(1, n + 1)
    ]


print(fizzBuzz(3))   # Output: ["1", "2", "Fizz"]
print(fizzBuzz(5))   # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(fizzBuzz(15))  # Output: ["1", "2", "Fizz", "4", "Buzz", ..., "14", "FizzBuzz"]
