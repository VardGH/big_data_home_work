import math

class Shape:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return "Generic Shape"

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def get_area(self):
        return math.pi * self._radius**2

    def get_perimeter(self):
        return 2 * math.pi * self._radius

    def __str__(self):
        return f"Circle (Radius: {self._radius})"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        self._side1 = value

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, value):
        self._side2 = value

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, value):
        self._side3 = value

    def get_area(self):
        p = (self._side1 + self._side2 + self._side3) / 2
        return math.sqrt(p * (p - self._side1) * (p - self._side2) * (p - self._side3))

    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3

    def __str__(self):
        return f"Triangle (Sides: {self._side1}, {self._side2}, {self._side3})"

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def get_area(self):
        return self._length * self._width

    def get_perimeter(self):
        return 2 * (self._length + self._width)

    def __str__(self):
        return f"Rectangle (Length: {self._length}, Width: {self._width})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square (Side: {self._length})"

# Function to print area and perimeter of a shape
def print_area_and_perimeter(shape):
    print(f"{shape}\nArea: {shape.get_area()}\nPerimeter: {shape.get_perimeter()}\n")

# CLI
def main():
    while True:
        try:
            print("Enter shape type and parameters.")
            input_str = input("Example: Circle 5, Triangle 3 4 5, Rectangle 3 4, Square 5: ")

            if input_str.lower() == "exit":
                break

            inputs = input_str.split()
            shape_type = inputs[0].lower()

            if shape_type == "circle":
                circle = Circle(float(inputs[1]))
                print_area_and_perimeter(circle)
            elif shape_type == "triangle":
                triangle = Triangle(float(inputs[1]), float(inputs[2]), float(inputs[3]))
                print_area_and_perimeter(triangle)
            elif shape_type == "rectangle":
                rectangle = Rectangle(float(inputs[1]), float(inputs[2]))
                print_area_and_perimeter(rectangle)
            elif shape_type == "square":
                square = Square(float(inputs[1]))
                print_area_and_perimeter(square)
            else:
                print("Invalid shape type.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()