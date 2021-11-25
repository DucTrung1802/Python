#-*-coding:utf-8-*-
# nhap vao pw - nhap vao chuoi pw
    #input: none
    #output: list password
import re
def inputPW():
    lstPW = input("Nhập mật khẩu(Cách nhau bằng dấu ','): ").split(", ")
    return lstPW
# kiem tra: do dai, a-z, A-Z, $#@
    #input: pw can check
    #output: pw hop le, neu pw ko hop le, phai tra ve tat ca nhung loi no gap phai
def checkPW(pwCheck):
    pwAfterCheck = pwCheck
    errorCheck = ""
    if len(pwCheck) < 6 or len(pwCheck) > 12:
        errorCheck = errorCheck + '1'
    if not re.search("[a-z]", pwCheck):
        errorCheck = errorCheck + '2'
    if not re.search("[0-9]", pwCheck):
        errorCheck = errorCheck + '3'
    if not re.search("[A-Z]", pwCheck):
        errorCheck = errorCheck + '4'
    if not re.search("[$#@]", pwCheck):
        errorCheck = errorCheck + '5'
 
    if (errorCheck != ""):
        pwAfterCheck = errorCheck

    print(pwAfterCheck)

    error_syntax = ""

    if len(errorCheck) == 0:
        error_syntax = pwCheck + " - ko loi"

    elif len(errorCheck) > 0:
        error_syntax = pwCheck + " - loi:"
        if '1' in errorCheck:
            error_syntax = error_syntax + " do dai"

        if '2' in errorCheck:
            error_syntax = error_syntax + " [a-z]"

        if '3' in errorCheck:
            error_syntax = error_syntax + " [0-9]"

        if '4' in errorCheck:
            error_syntax = error_syntax + " [A-Z]"

        if '5' in errorCheck:
            error_syntax = error_syntax + " [$#@]"


    print(error_syntax)
    print("-------------------")
    return pwAfterCheck
 
def main():
    # lst = inputPW()
    # print(lst)
    lstAfterCheck = []
    lst = ["linhdm", "linhdnm@12334", "Linhndm@123333", "dungda122", "Linhndm@123"]
    for item in lst:
        print(item)
        print("************")
        if checkPW(item) == item:
            lstAfterCheck.append(item)


    print(lstAfterCheck)
    # print(lstUpdate)
    #in ra dc cac pw hop le, cac pw loi phai tra ve nhung loi no gap p
if __name__ ==  "__main__":
    main()