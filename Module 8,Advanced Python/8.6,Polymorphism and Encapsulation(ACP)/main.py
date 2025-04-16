class square:
    def __init__(self,side):
        self.side = side

    def area(self):
        print("The area is :",self.side**2)

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("The area is :",3.14*self.radius**2)

square1 = square(10)
circle1 = circle(6)

for shape in (square1,circle1):
    shape.area()
