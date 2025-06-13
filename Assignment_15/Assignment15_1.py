import os

def main():

    print("Enter the filename you want to varify whether it exists or not: ")
    FileName = input()

    ret = os.path.exists(FileName)

    if (ret == True):
        print("File is present in current directory")
        

    else:
        print("No such file exists")    


if __name__ =="__main__":
    main()