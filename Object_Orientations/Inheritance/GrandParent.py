
'''
Method chaining is method in which it will call one method to the another method
'''
class GrandParent:
    def cook(self):
        print("GrandParent can cook Biriyani...")
class Parent(GrandParent):
    def cook(self):
        print("Parent can cook the rice....")
class Child(Parent):
    def cook(self):
        print("Children can't cook")
        super().cook()
        super(Parent,self).cook()
c = Child()
c.cook()
