'''
if abstract doesnt have any method then object for that abstract class can be created
'''

'''
if abstract class have only concrete method then object for that abstract class can be created and concrete methods can be invoked.
'''

class Demo1(ABC):
    pass

class Demo2(ABC):
    def disp2(self):
        print("Inside disp2")

class Demo3(ABC):
    def info(self):
        print("Inside info")
    @abstractmethod
    def disp3(self):
        print("Inside disp3")

class Demo4(Demo3):
    pass

d4 = Demo4()
d4.info()


# class Shape():
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         print("Logic to calculate area")
# class Circle():
#     def __init__(self, name):
#         self.name = name
#         super().__init__(name)
# c1 = Circle('Circle')
# c1.area()