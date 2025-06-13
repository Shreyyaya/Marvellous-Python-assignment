import os

def main():
    print("Enter the name of the file to write numbers 1 to 10:")
    file = input()

    f1 = open(file, "w")
    for i in range(1, 11):
        f1.write(str(i) + "\n")  # Write each number followed by a newline
        
    f1.close()

    print("Numbers 1 to 10 written to:", file)

if __name__ == "__main__":
    main()
