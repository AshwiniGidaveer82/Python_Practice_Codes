'''
In python we print reference variable then internally python will invoke __str__() which always returns string representations of an address of an object.
'''

class Demo1:
    def __str__(self):
        return 'Hello'
    def __add__(self, other):
        self.a = 20
        other.b = 30
        return self.a + other.b
class Demo2:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Akash'
d1 = Demo1()
d2 = Demo2()

print(d1)
print(d2)
print(d1 + d2)