import math
import cmath


class Solve_first_order_complex_equations(object):
    coe_1 = 0
    coe_2 = 0

    def __init__(self, coe_1, coe_2):
        self.coe_1 = coe_1
        self.coe_2 = coe_2
        print("Make Equation: %ax + %a = 0" %
              (self.coe_1, self.coe_2))

    def solve(self):
        if self.coe_1 == 0:

            if self.coe_2 == 0:
                print("Equation %ax + %a = 0 has infinite roots!" %
                      (self.coe_1, self.coe_2))

            elif self.coe_2 != 0:
                print("Equation %ax + %a = 0 has no roots!" %
                      (self.coe_1, self.coe_2))

        elif self.coe_1 != 0:

            if self.coe_2 == 0:
                root = self.coe_2/self.coe_1
                print("Equation %ax + %a = 0 has ONE root: %a" %
                      (self.coe_1, self.coe_2, root))

            elif self.coe_2 != 0:
                root = -self.coe_2/self.coe_1
                print("Equation %ax + %a = 0 has ONE root: %a" %
                      (self.coe_1, self.coe_2, root))


class Solve_second_order_complex_equations(object):
    coe_1 = 0
    coe_2 = 0
    coe_3 = 0

    def __init__(self, coe_1, coe_2, coe_3):
        self.coe_1 = coe_1
        self.coe_2 = coe_2
        self.coe_3 = coe_3
        print("Make Equation: %ax^2 + %ax + %a = 0" %
              (self.coe_1, self.coe_2, self.coe_3))

    def solve(self):
        if self.coe_1 == 0:

            if self.coe_2 == 0:

                if self.coe_3 == 0:
                    print("Equation %ax^2 + %ax + %a = 0 has infinite roots!" %
                          (self.coe_1, self.coe_2, self.coe_3))

                elif self.coe_3 != 0:
                    print("Equation %ax^2 + %ax + %a = 0 has no roots!" %
                          (self.coe_1, self.coe_2, self.coe_3))

            elif self.coe_2 != 0:

                if self.coe_3 == 0:
                    trivial_root = self.coe_3/self.coe_2
                    print("Equation %ax^2 + %ax + %a = 0 has ONE root: %a" %
                          (self.coe_1, self.coe_2, self.coe_3))

                elif self.coe_3 != 0:
                    self.root = -self.coe_3/self.coe_2
                    print("Equation %ax^2 + %ax + %a = 0 has ONE root: %a" %
                          (self.coe_1, self.coe_2, self.coe_3, trivial_root))

        elif self.coe_1 != 0:
            delta = pow(self.coe_2, 2) - 4*self.coe_1*self.coe_3

            if delta == 0:
                root_only = -self.coe_2/(2*self.coe_1)
                print("Equation %ax^2 + %ax + %a = 0 has ONE root: %a" %
                      (self.coe_1, self.coe_2, self.coe_3, root_only))

            else:
                root_complex_one = (-self.coe_2 +
                                    cmath.sqrt(delta))/(2*self.coe_1)
                root_complex_two = (-self.coe_2 +
                                    cmath.sqrt(delta))/(2*self.coe_1)
                print("Equation %ax^2 + %ax + %a = 0 has TWO roots: %a and %a" %
                      (self.coe_1, self.coe_2, self.coe_3, root_complex_one, root_complex_two))


def menu():
    print("______SOLVE EQUATIONS PROGRAM______")
    print()
    print("Choose your selection:")
    print("1. Solve First Order Complex Equation:  Ax + B = 0")
    print("2. Solve Second Order Complex Equation:  Ax^2 + Bx + C = 0")
    print("0. Exit Program")


def main():
    while True:
        print()
        menu()

        choose = input("Choose: ")

        if choose == '1':
            print("Form of Equation Ax + B = 0")
            a = input("A = ")
            b = input("B = ")
            e1 = Solve_first_order_complex_equations(complex(a), complex(b))
            e1.solve()

        if choose == '2':
            print("Form of Equation Ax^2 + Bx + C = 0")
            a = input("A = ")
            b = input("B = ")
            c = input("C = ")
            e2 = Solve_second_order_complex_equations(complex(a), complex(b), complex(c))
            e2.solve()

        elif choose == '0':
            break

        print()


if __name__ == "__main__":
    main()
