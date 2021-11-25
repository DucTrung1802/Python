import os
import time
import shutil

sourcePath = "C:/Users/ASUS/Desktop/Source_media"

def getModifiedTime(sourcePath):
    '''
    '''
    lstModTime = os.listdir(sourcePath)
    # print(lstModTime)
    #chay 1 vong for de lay ra thong tin cac file trong folder
    setModTime = set()
    for file in lstModTime:
        modificationTime = time.strftime('%d_%m_%Y', time.localtime(os.path.getmtime(sourcePath + "/" + file)))
        # print(modificationTime)
        setModTime.add(modificationTime)
    #Luu no vao 1 set
    return setModTime

def createFolderofTime(timeSet):
    sortDirectory = sourcePath + '/' + 'fileSorting'
    if not os.path.exists(sortDirectory):
        os.mkdir(sortDirectory)
        for entry in timeSet:
            os.mkdir(sortDirectory + '/' + entry)
        
def moveFiletoFolder():
    allfileTime = [file for file in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, file))]
    for file in allfileTime:
        modificationTime = time.strftime('%d_%m_%Y', time.localtime(os.path.getmtime(sourcePath + "/" + file)))
        #print(modificationTime)
        if os.path.exists(sourcePath + '/' + 'fileSorting' + '/' + modificationTime):
            shutil.copyfile(sourcePath + '/' + file, sourcePath + '/' + 'fileSorting' + '/' + modificationTime + '/'+ file)


def main():
    sourcePath = "C:/Users/ASUS/Desktop/Source_media"
    getSetTime = getModifiedTime(sourcePath)
    createFolderofTime(getSetTime)
    moveFiletoFolder()

if __name__ == "__main__":
    main()