# def disp():
#     return 10
#     return 20
#     return 30

# # res = disp()
# # print(res)

# print(disp())
# print(disp())
# print(disp())

def generator_function():
    print("Hello")
    yield 10
    yield 20
    yield 30
ref = generator_function()
print(next(ref))
print(next(ref))
print(next(ref))
print(next(ref))
# print(next(generator_function()))
# print(next(generator_function()))
# print(next(generator_function()))