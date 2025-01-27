class Employee:
    company_name = 'code'
    def __init__(self, name, age, desig):
        self.name = name
        self.age = age
        self.desig = desig

    def login(self, time):
        print(f"{self.name} logged in at {time}")

    def logout(self, time):
        print(f"{self.name} logged out at {time}")

    def work(self, hours):
        print(f"{self.name} logged in at {hours}")

    def getDetails(self):
        print("Employee Name ", self.name)
        print("Employee age ", self.age)
        print("Employee Designation ", self.desig)

e1 = Employee('AK','22','SDE')
e2 = Employee('PK','23','Manager')
e3 = Employee('RK','24','Developer')

e1.getDetails()
e2.getDetails()
e3.getDetails()