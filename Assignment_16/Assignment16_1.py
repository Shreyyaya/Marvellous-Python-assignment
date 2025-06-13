import os

def main():

    print("Enter the name of file that you want to write in: ")
    file = input()


    print("Enter content for: " ,file)       # Input and write to the file
    content = input()
    f1 = open(file, "w")
    f1.write(content)
    f1.close()  


if __name__ =="__main__":
    main() 