import re


def print_menu():
    print()
    print("Check password program")
    print(
        "Input password (multiple password can be accepted and must be split with comma [,]")
    print()


def check_password():
    valid_password_list = []
    
    # input_password = "ABd123,a F    1#,2w3E*,2We3345"
    input_password = input("Password(s): ")

    list_password = input_password.split(',')

    # Conditions: at least [a-z], [A-Z], \d = [0-9], space, @, #, $,
    # [A-Za-z\d @#$]{6,12}$ means the length is in interval 6 to 12
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[ @#$])[A-Za-z\d @#$]{6,12}$"

    pat = re.compile(reg)

    for password in list_password:
        
        valid = re.search(pat, password)

        if valid:
            valid_password_list.append(password)
        
    if len(valid_password_list):
        print("All valid password(s) are: ")

        for password in valid_password_list:
            print(password)

    elif not len(valid_password_list):
        print("There are not any valid passwords!")

    print()


def main():
    print_menu()

    check_password()


if __name__ == "__main__":
    main()
