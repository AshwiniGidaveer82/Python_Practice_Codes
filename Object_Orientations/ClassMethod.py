class Student:
    college_name = 'Kodnest'
    def get_info(self):
        print("College Name: ", Student.college_name)

    @classmethod
    def change_name(cls, new_name):
        cls.college_name = new_name

s1 = Student()
s1.get_info()
Student.change_name('Developer')
s1.get_info()