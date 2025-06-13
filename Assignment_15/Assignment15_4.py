import sys

def main():
    if len(sys.argv) < 3:
        print("python script.py file1 file2")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    print("Enter content for: " ,file1)       # Input and write to first file
    content1 = input()
    f1 = open(file1, "w")
    f1.write(content1)
    f1.close()

    print("Enter content for: ", file2)       # Input and write to second file
    content2 = input()
    f2 = open(file2, "w")
    f2.write(content2)
    f2.close()

    f1 = open(file1, "r")       # Read both files
    data1 = f1.read()
    f1.close()

    f2 = open(file2, "r")
    data2 = f2.read()
    f2.close()

    if data1 == data2:
        print("Success:Contents are same")   # Compare contents
    else:
        print("Failure:Contents are different")

if __name__ == "__main__":
    main()
