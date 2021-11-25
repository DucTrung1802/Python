import math

class Circle(object):

    def __init__(self, radius):
        if radius > 0:
            self.__radius = radius

        else:
            print("Invalid radius!")

    def get_radius(self):
        print(self.__radius)


    def perimeter(self):
        print(2*math.pi*self.__radius)

    def area(self):
        print(math.pi*self.__radius**2)

def main():
    circle_A = Circle(5)

    circle_A.get_radius()
    circle_A.perimeter()
    circle_A.area()


if __name__ == '__main__':
    main()