class Math(object):

    def __init__(self, first_number, second_number):
        self.__first_number = float(first_number)
        self.__second_number = float(second_number)

    def change_value(self, first_number, second_number):
        self.__first_number = float(first_number)
        self.__second_number = float(second_number)

    def sum(self):
        print(self.__first_number + self.__second_number)

    def subtract(self):
        print(self.__first_number - self.__second_number)

    def multiply(self):
        print(self.__first_number * self.__second_number)

    def divide(self):
        if self.__second_number != 0:
            print(self.__first_number / self.__second_number)

        else:
            print("The second number is equal to ZERO. Cannot divide!")


def main():
    math_A = Math(12, 20)

    math_A.change_value(5, 7)
    math_A.sum()
    math_A.subtract()
    math_A.multiply()
    math_A.divide()


if __name__ == '__main__':
    main()
