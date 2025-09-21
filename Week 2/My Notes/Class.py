h="Hello, \nFucking World"
print(h)

#Using class to find area of a Triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

b = eval(input("Enter base: "))
h = eval(input("Enter height: "))

A = Triangle(b, h)
print("Area of Triangle is: ", f"{A.area():.3f}")