import os

def DirectoryWatcher(DirectoryName, ext1, ext2):

    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("The path is invalid")
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")
        exit()

    print("Absolute path is: " + DirectoryName)
    print("Renaming all files with extension '" + ext1 + " to " + ext2 + "\n")

    count = 0
    for FolderName, SubFolderNames, Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            if fname.endswith(ext1):
                old_file = os.path.join(FolderName, fname)
                base, ext = os.path.splitext(fname)     
                if ext == ext1:
                    new_name = base + ext2
                new_file = os.path.join(FolderName, new_name)

                os.rename(old_file, new_file)
                print("Renamed: " + fname + " to " + new_name)
                count += 1

    if count == 0:
        print("No files found with the extension: " + ext1)
    else:
        print("\nTotal files renamed: " + str(count))

def main():
    print("Enter the name of directory you want to scan:")
    DirName = input()

    print("Enter the extension to search for:")
    ext1 = input()

    print("Enter the extension to rename to:")
    ext2 = input()

    DirectoryWatcher(DirName, ext1, ext2)

if __name__ == "__main__":
    main()
