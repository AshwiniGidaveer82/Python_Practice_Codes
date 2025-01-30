class Calculator:
    def calculate(self, a,b):
        pass

class Add(Calculator):
    def calculate(self, a, b):
        print("Addition:", a+b)

class Sub(Calculator):
    def calculate(self, a, b):
        print("Subtract:", a-b)

class Mul():
    pass

# def permit(ref, a, b):
#     if type(ref).__name__ == 'Mul':
#         print("Mul class does not have calculate()")
#     else:
#         ref.calculate(a, b)
# permit(Add(), 10, 20)
# permit(Sub(), 30, 20)
# permit(Mul(), 10, 5)

ref = Add(10, 20)
ref.calculate()

ref = Sub(10, 20)
ref.calculate()

ref = Mul(10, 20)
ref.calculate()