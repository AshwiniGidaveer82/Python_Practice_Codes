# def disp():
#     return 10
#     return 20
#     return 30

# # res = disp()
# # print(res)

# print(disp())
# print(disp())
# print(disp())

# def generator_function():
#     print("Hello")
#     yield 10
#     yield 20
#     yield 30
# ref = generator_function()
# print(next(ref))
# print(next(ref))
# print(next(ref))
# print(next(ref))
# print(next(generator_function()))
# print(next(generator_function()))
# print(next(generator_function()))

def  fibonacci(num):
    a,b = 0,1
    for i in range(num):
        print(a)
        a,b = b, a+b
fibonacci(10)

def  fibonacci_gen(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = b, a+b
ref = fibonacci_gen(100)
print(next(ref))
print(next(ref))