def main():
    print("Enter the name of the file to clean:")
    source = input()
    destination = "cleaned.txt"

    # Open source for reading and destination for writing
    ifile = open(source, "r")
    ofile = open(destination, "w")

    for line in ifile:
        if line.strip() != "":  #if line is not blank
            ofile.write(line)

    ifile.close()
    ofile.close()

    print("Blank lines removed. Cleaned content written to cleaned.txt file.")

if __name__ == "__main__":
    main()
