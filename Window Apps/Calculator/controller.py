from view import *
from model import *
from math import sqrt


def sqr(x):
    return x**2


class CONTROLLER:

    def __init__(self):
        self.view = VIEW(self)
        self.model = MODEL(self)

        # Initialize values
        self.operands = [0, None]       # for calculating
        self.operand_index = 0
        self.operands_text = ["", ""]   # for displaying
        self.new_operand = False
        self.operators = ["", ""]
        self.operator_index = 0
        self.can_erase = False
        self.isaccumulate = False
        self.old_calculation = False
        # Includes square root of negative number and 1/zero
        self.invalid_expression = False

        # List for easier if-else
        self.unary_operators = {"\u215f", "x\u00b2", "\u221ax"}
        self.binary_operators = {"+", "-", "\u00d7", "\u00f7"}
        self.special_operators = {"%", "CE", "C", "\u232b"}
        self.all_operators = set.union(
            self.unary_operators, self.binary_operators, self.special_operators)
        self.operand_symbol = ['0', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9', '.', "\u00b1"]

    def start_app(self):
        self.view.init_display()

    def button_trigger(self, button_name):
        """
        Process when user click on buttons
        """

        # Reset if invalid_expression
        if self.invalid_expression and button_name not in self.operand_symbol:
            self.reset_all()

        # Operand symbol are numbers from 0-9 and decimal point "."
        elif button_name in self.operand_symbol:
            # Reset if divide zero but include one digit
            if self.invalid_expression:
                self.reset_with_new_digit(button_name)
                return

            # Make a new calculation
            elif self.old_calculation and button_name != "\u00b1":
                self.reset_all()

            self.isaccumulate = False

            # Continously press "0" while input is already "0",
            if not self.operands_text[self.operand_index] and button_name == "0":
                self.operands_text[self.operand_index] = ""
                return

            elif button_name == ".":
                # Press decimal point button while input is "0"
                if self.operands_text[self.operand_index] == "":
                    self.operands[self.operand_index] = 0
                    self.operands_text[self.operand_index] = str(
                        self.operands[self.operand_index])
                    self.view.insert_main_line(
                        self.operands_text[self.operand_index] + ".")

                if "." in self.operands_text[self.operand_index]:
                    return
                else:
                    self.operands_text[self.operand_index] += "."
                    self.view.insert_main_line(
                        str(self.operands[self.operand_index]) + ".")
                    return

            elif button_name == "\u00b1":
                # Change sign does not work with zero
                if self.operands[self.operand_index] == 0:
                    return

                if self.old_calculation:
                    self.operand_index = 0
                    self.operands[self.operand_index] = eval(
                        self.operands_text[self.operand_index])
                    self.view.insert_subline(
                        "negate(" + self.operands_text[self.operand_index] + ")")

                self.operands[self.operand_index] *= -1
                self.operands_text[self.operand_index] = str(
                    self.operands[self.operand_index])
                self.view.insert_main_line(
                    self.operands[self.operand_index])
                return

            else:
                # If self.can_erase is True, Erase button can be pressed
                # It means while we are inputting number, we can delete each undesired number
                self.can_erase = True

            # Accumulate input number
            self.operands_text[self.operand_index] += button_name
            self.operands[self.operand_index] = eval(
                self.operands_text[self.operand_index])

            # Display number
            self.view.insert_main_line(self.operands[self.operand_index])

        # If operator button is pressed
        elif button_name in self.all_operators:
            self.isaccumulate = False
            self.old_calculation = False
            self.operators[self.operator_index] = button_name

            # If operator is unary operator
            if self.operators[self.operator_index] in self.unary_operators:

                self.can_erase = False

                if self.operator_index == 0:
                    subexpression = ""
                elif self.operator_index == 1:
                    subexpression = self.operands_text[0] + \
                        " " + self.operators[0] + " "

                # \u215f: Fraction Numerator One
                if self.operators[self.operator_index] == "\u215f":
                    # If denominator is zero -> Error
                    if self.operands[self.operand_index] == 0:
                        self.view.insert_subline(subexpression + "1/(0)")
                        self.view.error(-8, "Cannot divide by zero")
                        self.invalid_expression = True

                    # Else: work normally
                    else:
                        expression = "1/(" + \
                            self.operands_text[self.operand_index] + ")"
                        self.view.insert_subline(subexpression + expression)
                        self.operands[self.operand_index] = eval(expression)
                        self.view.insert_main_line(
                            self.operands[self.operand_index])
                        self.operands_text[self.operand_index] = expression
                        return

                # x\u00b2: x squared
                if self.operators[self.operator_index] == "x\u00b2":
                    # Press squared button for second operand but without input, take the first operand as input
                    # For example: press "3 + sqr()"
                    if self.operands[self.operand_index] == 0 or not self.operands[self.operand_index]:
                        self.operands[self.operand_index] = self.operands[0]
                        self.view.insert_subline(
                            subexpression + "sqr(" + str(self.operands[self.operand_index]) + ")")
                        self.operands[self.operand_index] *= self.operands[self.operand_index]
                        self.operands_text[self.operand_index] = str(
                            self.operands[self.operand_index])
                        self.view.insert_main_line(
                            str(self.operands[self.operand_index]))
                        return

                    expression = "sqr(" + \
                        self.operands_text[self.operand_index] + ")"
                    self.view.insert_subline(subexpression + expression)
                    self.operands[self.operand_index] = eval(expression)
                    self.view.insert_main_line(
                        self.operands[self.operand_index])
                    self.operands_text[self.operand_index] = expression
                    return

                # \u221ax: Square Root of x
                if self.operators[self.operator_index] == "\u221ax":
                    # Press squared button for second operand but without input, take the first operand as input
                    # For example: press "3 + sqrt()"
                    if self.operands[self.operand_index] == 0 or not self.operands[self.operand_index]:
                        self.operands[self.operand_index] = self.operands[0]
                        self.view.insert_subline(
                            subexpression + "sqrt(" + str(self.operands[self.operand_index]) + ")")
                        self.operands[self.operand_index] = sqrt(
                            self.operands[self.operand_index])
                        self.operands_text[self.operand_index] = str(
                            self.operands[self.operand_index])
                        self.view.insert_main_line(
                            str(self.operands[self.operand_index]))
                        return

                    # Square root does not work with negative numbers
                    elif self.operands[self.operand_index] < 0:
                        self.view.insert_subline(
                            subexpression + "sqrt("+str(self.operands[self.operand_index])+")")
                        self.view.insert_main_line("0")
                        self.view.error(0, "Invalid input")
                        self.invalid_expression = True
                        return

                    # Make size of output smaller since square root usually has several numbers after decimal point
                    self.view.configure_main_line_size(-10)

                    # Work normally
                    expression = "sqrt(" + \
                        self.operands_text[self.operand_index] + ")"
                    self.view.insert_subline(subexpression + expression)
                    self.operands[self.operand_index] = eval(expression)
                    self.view.insert_main_line(
                        self.operands[self.operand_index])
                    self.operands_text[self.operand_index] = expression
                    return

            # If operator is binary operator
            if self.operators[self.operator_index] in self.binary_operators:

                # Input is "0", press decimal point button but press operator button immediately
                if not self.operands_text[0] or self.operands_text[0] == "0.":
                    self.operands_text[0] = "0"
                    self.view.insert_main_line(self.operands[0])

                # Automatically calculate the binary expression if there is sufficient data
                # For example: press "3 + 6 +""
                if self.operator_index == 1 and self.operands_text[1]:
                    # calculate() covered "+", "-", "*", "/"
                    self.calculate()
                    self.view.insert_subline(
                        self.operands_text[0] + " " + self.operators[0])
                    self.view.insert_main_line(self.operands[0])

                else:
                    # Change the operator if the second operand has not been input
                    if not self.operands_text[1]:
                        self.operators[0] = button_name
                        self.operators[1] = ""
                        self.view.insert_subline(
                            self.operands_text[0] + " " + self.operators[0])
                        self.operand_index = 1
                        self.operator_index = 1
                        return

            # If
            if self.operators[self.operator_index] in self.special_operators:

                # Clear all the inputting numbers
                if self.operators[self.operator_index] == "CE":
                    # If the first operand is inputting, clear all the operand
                    # For example: press "3333 CE"
                    if not self.operator_index:
                        self.operators[self.operator_index] = ""
                        self.operands[0] = 0
                        self.operands_text[0] = ""

                    # If the second operand is inputting, clear all the operand but remain the expression
                    # For example: press "3333 + CE" or "3333 + 666666 CE"
                    else:
                        self.operands_text[1] = ""
                        self.operands[1] = 0
                        self.view.insert_subline(
                            self.operands_text[0] + " " + self.operators[0])

                    self.view.insert_main_line("0")

                # Reset button
                elif self.operators[self.operator_index] == "C":
                    self.reset_all()

                elif self.operators[self.operator_index] == "%":

                    # Only one operand
                    if self.operator_index == 0:
                        self.operands_text[0] = ""
                        self.operands[0] = 0
                        self.view.insert_subline("0")
                        self.view.insert_main_line("0")

                    else:
                        # Press binary operator button but no second operand, the second operand will be the first operand
                        if not self.operands_text[1]:
                            self.operands_text[1] = self.operands_text[0]

                        if self.operators[0] in ["+", "-"]:
                            result = eval(
                                self.operands_text[0] + "*" + self.operands_text[1]) / 100
                            self.operands[1] = result
                            self.operands_text[1] = str(self.operands[1])
                            self.view.insert_main_line(self.operands[1])
                            self.view.insert_subline(
                                self.operands_text[0] + " " + self.operators[0] + " " + self.operands_text[1])

                        else:
                            result = eval(self.operands_text[1]) / 100
                            self.operands[1] = result
                            self.operands_text[1] = str(self.operands[1])
                            self.view.insert_main_line(self.operands[1])
                            self.view.insert_subline(
                                self.operands_text[0] + " " + self.operators[0] + " " + self.operands_text[1])

                # Erase to the left button
                elif self.operators[self.operator_index] == "\u232b":
                    # Only available while inputting numbers
                    if self.can_erase:
                        length = len(self.operands_text[self.operand_index])
                        if length <= 1:
                            self.operands_text[self.operand_index] = ""
                            self.operands[self.operator_index] = 0
                        else:
                            self.operands_text[self.operand_index] = self.operands_text[self.operand_index][0:length-1]
                            self.operands[self.operand_index] = eval(
                                self.operands_text[self.operand_index])

                        self.view.insert_main_line(
                            self.operands[self.operand_index])

        elif button_name == "=":

            self.old_calculation = True
            
            # The fisrt operand is zero and the second operand is not input
            if self.operands_text[0] == "0" or self.operands_text[0] == "0." or not self.operands_text[0]:
                self.operands[0] = 0
                self.operands_text[0] = str(self.operands[0])
                self.view.insert_subline(self.operands_text[0] + " " + "=")
                self.view.insert_main_line(self.operands[0])

            # The fisrt operand is input and the second operand is not input  
            elif not self.operators[0]:
                self.view.insert_subline(self.operands_text[0] + " " + "=")
                self.view.insert_main_line(self.operands[0])

            # The fisrt operand is input with unary operator       
            elif self.operators[0] in self.unary_operators:
                self.view.insert_subline(self.operands_text[0] + " " + "=")
                self.view.insert_main_line(self.operands[0])
                self.operands_text[0] = str(self.operands[0])

            # The fisrt operand is input with binary operator       
            elif self.operators[0] in self.binary_operators:
                # Check if the second operand is None
                if not self.operands[1] and self.operands[1] != 0:
                    if not self.isaccumulate:
                        self.fixed_operand = eval(self.operands_text[0])

                    if self.operators[0] == "\u00d7":
                        real_operator = "*"
                    elif self.operators[0] == "\u00f7":
                        real_operator = "/"
                    else:
                        real_operator = self.operators[0]

                    self.view.insert_subline(
                        self.operands_text[0] + " " + self.operators[0] + " " + str(self.fixed_operand) + " " + "=")
                    result = eval(
                        self.operands_text[0]+real_operator+str(self.fixed_operand))
                    self.operands_text[0] = str(result)
                    self.view.insert_main_line(eval(self.operands_text[0]))
                    self.isaccumulate = True
                    # continue

                # The second operand is input
                else:
                    self.operands_text[1] = str(self.operands[1])
                    self.fixed_operand = self.operands_text[1]
                    self.isaccumulate = True
                    save_operators = self.operators[0]
                    self.view.insert_subline(
                        self.operands_text[0] + " " + self.operators[0] + " " + self.operands_text[1] + " " + "=")
                    self.calculate()
                    self.operators[0] = save_operators
                    self.view.insert_main_line(self.operands[0])

    def reset_with_new_digit(self, new_digit):
        self.view.insert_subline("")
        self.reset_all()
        self.operands_text[self.operand_index] += new_digit
        self.operands[self.operand_index] = eval(
            self.operands_text[self.operand_index])
        self.view.insert_main_line(self.operands[self.operand_index])

    def reset_all(self):
        self.operands = [0, None]
        self.operand_index = 0
        self.operands_text = ["", ""]
        self.new_operand = False
        self.operators = ["", ""]
        self.operator_index = 0
        self.can_erase = False
        self.isaccumulate = False
        self.old_calculation = False
        self.invalid_expression = False

        self.view.insert_subline("")
        self.view.insert_main_line("0")

        # Reset state of buttons:
        for i in range(23):
            self.view.standard_frame.calculating_button_frame.calculating_buttons[
                i]['state'] = "normal"

        self.view.configure_main_line_size(0)

    def calculate(self):
        self.can_erase = False
        if self.operators[0] == "\u00d7":
            self.operators[0] = "*"
        elif self.operators[0] == "\u00f7":
            self.operators[0] = "/"

        result_text = self.operands_text[0] + \
            self.operators[0] + self.operands_text[1]
        self.operands[0] = eval(result_text)
        self.operands_text[0] = str(self.operands[0])
        self.operands[1] = None
        self.operands_text[1] = ""
        self.operators[0] = self.operators[1]
        self.operators[1] = ""
        self.operator_index = 1


def main():
    app = CONTROLLER()
    app.start_app()


if __name__ == "__main__":
    main()
