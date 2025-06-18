import os
import time
import sys
import hashlib


def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path, 'rb')

    hobj = hashlib.md5()  #md5 is an algo

    buffer = fobj.read(BlockSize)  
    while(len(buffer) > 0):
        hobj.update(buffer) 
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


def DirectoryWatcher(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)      


    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The path is invalid")            
        exit()
    

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is valid but the target is not a directory")   
        exit()

    for FolderName, SubFolderNames, Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)
            print("Filename: ", fname)
            print("Checksum: ", checksum)
            print()
                

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename, "w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is a log file of marvellous automation script \n")
    fobj.write("This is a directory cleaner script \n")

    fobj.write(Border+"\n")
    fobj.write("File is created at: "+timestamp+"\n")
    fobj.write(Border+"\n")

def FindDuplicate(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)      


    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The path is invalid")            
        exit()
    

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is valid but the target is not a directory")   
        exit()

    Duplicate = {}    

    for FolderName, SubFolderNames, Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            if (checksum in Duplicate):
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]     

    return Duplicate            
 
def DisplayResult(MyDict):
    result = list(filter(lambda x: len(x) >  1 , MyDict.values()))

    count = 0

    for value in result:
        for subvalue in value:
            count = count + 1 
            print(subvalue)
            

        print("-----------------------------------------------------------")
        print("Value of count is:", count)
        print("-----------------------------------------------------------")
        count = 0 
        

def DeleteDuplicate(MyDict):
    result = list(filter(lambda x: len(x) >  1 , MyDict.values()))

    count = 0
    Cnt = 0

    for value in result:
        for subvalue in value:
            count = count + 1 
            if (count > 1):
                print("Deledted file: ", subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1

        count = 0 

        
                
    print("Total deleted file:", Cnt)

def main():
  
    border = "-"*54
    
    print(border)
    print("----------------Marvellous Automation-----------------")
    print(border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to perform Directory cleaning")
            print("This is the directory automation script")

        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U") :
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")

        else:
            result = FindDuplicate(sys.argv[1])  
            DeleteDuplicate(result)

            
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : used to display help")
        print("--u : used to display the usage") 


    print(border)
    print("-----------Thank you for using our script-------------")
    print("---------------Marvellous Infosystems-----------------")
    print(border)


if __name__ == "__main__":
    main()    