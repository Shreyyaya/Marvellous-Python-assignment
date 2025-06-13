import os

def main():
    print("Enter the name of the file:")
    filename = input()

    if os.path.exists(filename):
        f = open(filename, "r")
        content = f.read()
        f.close()
    else:
        print("File doesnt exist. Creating new file:", filename)
        print("Enter content for the file:")
        content = input()

        f = open(filename, "w")
        f.write(content)
        f.close()

    # Count lines, words, characters
    lines = content.splitlines()
    words = content.split()
    char = len(content)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", char)

if __name__ == "__main__":
    main()
