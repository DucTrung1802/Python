
import os
import os.path
from time import sleep

def sort_files(current_directory):
    from os import path
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory = current_directory + "/"

 # current_directory đang là hardcode, cần sửa đổi để người dùng import vào
 # cần có Menu

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
        # Kiểm tra thư mục có tên extension đã tồn tại hay chưa
        if path.isdir(current_directory+extension) == False:
            os.mkdir(current_directory+extension)

    # Di chuyển các file có extension về các thư mục tương ứng
    for file in all_files:
        # Chỉ di chuyển file
        if os.path.isfile(current_directory+file) == True:
            if file != "Sort_Files_In_Folders.exe":
                file_name, file_extension = os.path.splitext(
                    current_directory + file)
                os.rename(current_directory + file,
                          current_directory+file_extension+"/"+file)


def main():

    print()
    print("________SORT FILE IN CORRESPONDING FOLDER________")
    print()
    print("Choose your selection: ")
    print("1. Sort")
    print("2. Exit")
    choose = input("Choose: ")
    print()

    if choose == '1':
        folder_path = input("Input the path of folder you want to sort: ")

        if os.path.exists(folder_path) == True:
            print("Saving...")
            sort_files(folder_path)
            print("Thank you for using this program!")
            input("Press Enter to continue...")

        else:
            print("Your path does not exist!")
            input("Press Enter to continue...")

    elif choose == '2':
        print("No problem. You may need this program later")
        sleep(2)
        exit(1)


# os.mkdir(current_directory + file.lower())
if __name__ == "__main__":
    main()
