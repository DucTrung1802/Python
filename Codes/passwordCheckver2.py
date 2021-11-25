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
    errorList = []
    if len(pwCheck) < 6 or len(pwCheck) > 12:
        errorCheck = errorCheck + '1'
        errorList.append("Do dai")
    if not re.search("[a-z]", pwCheck):
        errorCheck = errorCheck + '2'
        errorList.append("[a-z]")
    if not re.search("[0-9]", pwCheck):
        errorCheck = errorCheck + '3'
        errorList.append("[0-9]")
    if not re.search("[A-Z]", pwCheck):
        errorCheck = errorCheck + '4'
        errorList.append("[A-Z]")
    if not re.search("[$#@]", pwCheck):
        errorCheck = errorCheck + '5'
        errorList.append("[$#@]")
    
    listToStr = ' '.join(map(str,errorList))
    
    if (errorCheck != ""):
        pwAfterCheck = errorCheck
        print("loi " + listToStr)
    else:
        print("Mat khau hop le")
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