# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.


class Rectangle(object):
    def __init__(self, length, width):
        if (length > width):
            self._length = length
            self._width = width

        else:
            self._length = width
            self._width = length

    def perimeter(self):
        return (self._length+self._width)*2

    def area(self):
        return self._length*self._width

    def display(self):
        print("Length =  %.2f" % (self._length))
        print("Width = %.2f" % (self._width))
        print("Perimeter = %.2f" %(self.perimeter()))
        print("Area = %.2f" %(self.area()))

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self._height = height

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()

    def volume(self):
        return (self._length*self._width*self._height)

    def display(self):
        super().display()
        print("Volume = %.2f" %(self.volume()))

def main():

    a = Rectangle(5, 3)
    # print(a.perimeter())
    # print(a.area())
    a.display()

    print()

    b = Parallelepipede(8, 5, 9)
    # print(b.volume())
    b.display()

if __name__ == '__main__':
    main()    
