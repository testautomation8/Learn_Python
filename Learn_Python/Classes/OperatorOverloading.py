class Vector:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Vector(real, imag)

    def __str__(self):
        return "{}i + {}j".format(self.real, self.imag)


num1 = Vector(2, 3)
num2 = Vector(4, 5)
num3 = num1 + num2  # This is equivalent to num3.__add__(num1, num2)
print(num1)
print(num2)
print(num3)
