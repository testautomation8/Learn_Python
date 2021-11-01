class Student:

    """I am Student class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hi! I am {} and my age is {}".format(self.name, self.age))


print(Student.__doc__)
student_1 = Student("Jack Sparrow", 35)
student_1.intro()

