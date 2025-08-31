import math

class Shape:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

def main():
    shapes = [
        Rectangle(3, 4, "red"),
        Circle(2.5, "blue"),
        Rectangle(6, 2, "green")
    ]

    for shape in shapes:
        print(f"Color: {shape.get_color()}")
        
        if isinstance(shape, Rectangle):
            print(f"Area: {shape.area()}")
            print(f"Perimeter: {shape.perimeter()}")
        elif isinstance(shape, Circle):
            print(f"Area: {shape.area():.2f}") 
            print(f"Circumference: {shape.circumference():.2f}")
        
        print()

if __name__ == "__main__":
    main()