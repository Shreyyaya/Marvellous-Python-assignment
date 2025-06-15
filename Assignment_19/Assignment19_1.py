import os

def DirectoryWatcher(DirectoryName, Extension):

    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)      

    if not os.path.exists(DirectoryName):
        print("The path is invalid")            
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")   
        exit()

    print("Absolute path is: " + DirectoryName)
    print("files with extension: " + Extension)

    found = False
    for FolderName, SubFolderNames, Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            if fname.endswith(Extension):
                print("File name is: " + fname)
                found = True

    if not found:
        print("No files found with the extension: " + Extension)

def main():
    print("Enter the name of directory you want to search:")
    DirName = input()

    print("Enter the file extension to look for:")
    Extension = input()

    DirectoryWatcher(DirName, Extension)

if __name__ == "__main__":
    main()
