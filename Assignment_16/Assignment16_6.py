import sys

def main():
    if len(sys.argv) < 3:
        print("python script.py YourFileNmae.txt Demo.txt")
        return

    source_file = sys.argv[1]
    Destination_file = sys.argv[2]

    print("Enter the content to write into: ", source_file)
    content = input()

    # Create and write to user named file
    f1 = open(source_file, "w")
    f1.write(content)
    f1.close()
    print("Data written to:" ,source_file)

    # Read from source and write to demo
    f1 = open(source_file, "r")
    data = f1.read()
    f1.close()

    f2 = open(Destination_file, "w")
    f2.write(data)
    f2.close()

    print("Data successfully copied to: ", Destination_file)

if __name__ == "__main__":
    main()
