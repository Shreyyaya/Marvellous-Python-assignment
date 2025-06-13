def main():
    print("Enter the name of the file:")
    filename = input()

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    f = open(filename, "r")
    print("\nLines with more than 5 words:\n")

    for line in f:
        words = line.split()
        if len(words) > 5:
            print(line.strip())

    f.close()

if __name__ == "__main__":
    import os
    main()
