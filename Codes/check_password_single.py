import re


def print_menu():
    print()
    print("Check password program")
    print()





def check_password():
    # Some conditions to check:
    invalid_lowercase_letters = False
    invalid_uppercase_letters = False
    invalid_numbers = False
    invalid_special_characters = False


    input_password = input("Password: ")

    # Conditions: at least [a-z], [A-Z], \d = [0-9], space, @, #, $,
    # [A-Za-z\d @#$]{6,12}$ means the length is in interval 6 to 12
    # reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[ @#$])[A-Za-z\d @#$]{6,12}$"

    invalid_lowercase_letters = not re.search("[a-z]", input_password)

    invalid_uppercase_letters = not re.search("[A-Z]", input_password)

    invalid_numbers = not re.search("[0-9]", input_password)

    invalid_special_characters = not re.search("[$#@ ]", input_password)

    
    # Check conditions:

    if not 6 <= len(input_password) <= 12:
        print("The length of password must be 6-12!")

    if invalid_lowercase_letters == True:
        print("The password need at least ONE lowercase letter!")
    
    if invalid_uppercase_letters == True:
        print("The password need at least ONE uppercase letter!")
    
    if invalid_numbers == True:
        print("The password need at least ONE number!")
    
    if invalid_special_characters == True:
        print("The password need at least one of these character(s): @, #, $, 'space'!")

    else: 
        print("The password is VALID!")


def main():
    print_menu()

    check_password()


if __name__ == "__main__":
    main()
