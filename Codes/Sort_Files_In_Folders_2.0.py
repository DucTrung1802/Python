# List all drives: https://www.daniweb.com/programming/software-development/threads/518063/how-to-list-the-name-and-the-size-of-hard-driver-in-python

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


import os
import string
from ctypes import windll
import os.path


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')


# # sleep for 2 seconds after printing output
# sleep(2)

# # now call function we defined above
# clear()


path = ""
list_drive_convert = []
list_entry = []
list_directory = []
choose = 0


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def set_path():
    global path
    global list_entry
    global list_directory

    path = ""

    if (list_entry != []):
        # print(list_entry)
        for entry in list_entry:
            path = path + entry + "/"


def menu():
    global list_directory

    print()
    print("_________Sort Files In Folders 2.0_________")
    print()
    print("Menu:")
    print("[order of folder]: Open that folder")
    print("b: Back")
    print("c: Choose")
    print("e: Exit program")
    print()

    if (path != ""):
        print()
        print("PATH: ", end=path)
        print("\n")
        print()

        test_directory_exist = []
        for entry in os.listdir(path):
            if (os.path.isdir(path+entry) == True):
                test_directory_exist.append(entry)
                break

        if (test_directory_exist == []):
            print("This path does not contain any folders!")
            print()
            list_directory = []

        else:
            print("Entries in this path (with order: folder; without order: file):")
            print()
            list_directory = []
            for entry in os.listdir(path):
                if (os.path.isdir(path+entry) == True):
                    list_directory.append(entry)
                    print(str(list_directory.index(entry)+1) + ". " + entry)

            for entry in os.listdir(path):
                if (os.path.isdir(path+entry) == False):
                    print("_. " + entry)


def sort_files(current_directory):
    from os import path
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory = current_directory + "/"

 # current_directory ??ang l?? hardcode, c???n s???a ?????i ????? ng?????i d??ng import v??o
 # c???n c?? Menu

    all_files = os.listdir(current_directory)
    # print(all_files)
    list_extension = list()

    for file in all_files:
        # print(file)
        file_name, file_extension = os.path.splitext(current_directory + file)
        # print(file_name)
        # print("_________")
        # print(file_extension)
        list_extension.append(file_extension)

    set_extension = set(list_extension)
    # print(set_extension)

    # for extension in set_extension:
    #     if extension == "":
    #         continue

    list_extension_convert = list(set_extension)
    # os.mkdir(current_directory + extension)

    list_extension_convert.remove("")

    # print(list_extension_convert)

    for extension in list_extension_convert:
        # print(path.isdir(extension))
        # Ki???m tra th?? m???c c?? t??n extension ???? t???n t???i hay ch??a
        if path.isdir(current_directory+extension) == False:
            os.mkdir(current_directory+extension)

    # Di chuy???n c??c file c?? extension v??? c??c th?? m???c t????ng ???ng
    for file in all_files:
        # Ch??? di chuy???n file
        if os.path.isfile(current_directory+file) == True:
            if file != "Sort_Files_In_Folders.exe":
                file_name, file_extension = os.path.splitext(
                    current_directory + file)
                os.rename(current_directory + file,
                          current_directory+file_extension+"/"+file)


def main():
    global choose
    global list_entry
    global path
    global list_directory

    list_drives = get_drives()

    for drive in list_drives:
        drive = drive+":"
        # print(drive)
        list_drive_convert.append(drive)

    # print(list_drive_convert)

    list_drives = list_drive_convert
    # print(list_drives)

    while(choose != 'e'):
        menu()

        if (list_entry == []):
            for drive in list_drives:
                print(str(list_drives.index(drive)+1) + ". " + drive)

        print()
        choose = input("Choose your selection: ")

        if ((list_entry == []) and (choose == 'b')):
            print("\nCannot get back from here!")
            input("\nPress any key to continue...")
            clear()
            continue

        if ((list_entry != []) and (choose == 'b')):
            clear()
            list_entry.pop()
            set_path()
            continue

        if (list_entry != [] and choose == 'c'):
            print("Do you want to sort all FILES in this PATH: ", end=path+"?\n")
            print("Y. Yes")
            print("N. No")
            sort_decision = input("Choose: ")

            if (sort_decision == 'y'):
                print("Sorting...")
                sort_files(path)
                sleep(1)
                print("DONE!")
                continue

            else:
                continue

        if (choose == 'e'):
            print()
            print("Thank you for using the program!")
            print("The program will end in 2 seconds!")
            sleep(2)
            exit(1)

        if (list_entry == [] and choose.isnumeric()):
            for drive in list_drives:
                index = int(choose)-1

                if (0 <= index < len(list_drives)):
                    list_entry.append(list_drives[index])
                    set_path()
                    break

                else:
                    print()
                    print("Out of range!")
                    input("\nPress any key to continue...")
                    break

            continue

        if (list_entry != [] and choose.isnumeric()):

            for entry in list_directory:
                index = int(choose)-1

                if (0 <= index < len(list_directory)):
                    list_entry.append(list_directory[index])
                    set_path()
                    break

                else:
                    print()
                    print("Out of range!")
                    input("\nPress any key to continue...")
                    break

        else:
            print()
            print("Invalid selection!")
            input("\nPress any key to continue...")

        clear()


    # print(os.listdir(list_drives[0]))
if __name__ == '__main__':
    main()


# import os

# # List all files in a directory using os.listdir
# basepath = 'D:/'
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         print(entry)
