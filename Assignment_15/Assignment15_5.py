import os

def main():
    print("Enter the file name:")
    filename = input()

    print("Enter string to search:")
    str = input()

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    f = open(filename, "r")    # Open file and read content
    content = f.read()
    f.close()

    count = content.count(str)

    print("The string occurred this times in the file: ", count)

if __name__ == "__main__":
    main()
