import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("Point at", (self.x, self.y))


# Line class
class Line(Shape):
    def __init__(self, start, end):
        self.start = start  
        self.end = end      

    def area(self):
        return 0

    def perimeter(self):
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)

    def draw(self):
        print("Line from", (self.start.x, self.start.y), "to", (self.end.x, self.end.y))


class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        b = math.sqrt((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)
        c = math.sqrt((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)
        s = (a + b + c) / 2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

    def perimeter(self):
        a = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        b = math.sqrt((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)
        c = math.sqrt((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)
        return a + b + c

    def draw(self):
        print("Triangle at points", (self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y))


class Rectangle(Shape):
    def __init__(self, top_left, width, height):
        self.top_left = top_left  
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print("Rectangle at top-left", (self.top_left.x, self.top_left.y), 
              "width", self.width, "height", self.height)


class Square(Rectangle):
    def __init__(self, top_left, side):
        super().__init__(top_left, side, side)

    def draw(self):
        print("Square at top-left", (self.top_left.x, self.top_left.y), "side", self.width)


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        print("Circle at center", (self.center.x, self.center.y), "radius", self.radius)


class Pentagon(Shape):
    def __init__(self, center, side):
        self.center = center
        self.side = side

    def area(self):
        return (5 * self.side**2) / (4 * math.tan(math.pi/5))

    def perimeter(self):
        return 5 * self.side

    def draw(self):
        print("Pentagon at center", (self.center.x, self.center.y), "side", self.side)


class Quadrilateral(Shape):
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        x = [self.p1.x, self.p2.x, self.p3.x, self.p4.x]
        y = [self.p1.y, self.p2.y, self.p3.y, self.p4.y]
        return 0.5 * abs(x[0]*y[1] + x[1]*y[2] + x[2]*y[3] + x[3]*y[0] -
                         y[0]*x[1] - y[1]*x[2] - y[2]*x[3] - y[3]*x[0])

    def perimeter(self):
        a = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        b = math.sqrt((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)
        c = math.sqrt((self.p4.x - self.p3.x)**2 + (self.p4.y - self.p3.y)**2)
        d = math.sqrt((self.p1.x - self.p4.x)**2 + (self.p1.y - self.p4.y)**2)
        return a + b + c + d

    def draw(self):
        print("Quadrilateral at points", (self.p1.x, self.p1.y), (self.p2.x, self.p2.y),
              (self.p3.x, self.p3.y), (self.p4.x, self.p4.y))


if __name__ == "__main__":
    p1 = Point(0,0)
    p2 = Point(2,0)
    p3 = Point(0,5)
    p4 = Point(4,3)
    p5 = Point(4,10)

    line = Line(p1, p2)
    triangle = Triangle(p1, p2, p3)
    rectangle = Rectangle(p1, 4, 3)
    square = Square(p1, 5)
    circle = Circle(p5, 3)
    pentagon = Pentagon(p5, 2)
    quadrilateral = Quadrilateral(p1, p2, p4, p3)

    shapes = [line, triangle, rectangle, square, circle, pentagon, quadrilateral]

    for shape in shapes:
        shape.draw()
        print("Area", shape.area())
        print("Perimeter", shape.perimeter())
        print()
