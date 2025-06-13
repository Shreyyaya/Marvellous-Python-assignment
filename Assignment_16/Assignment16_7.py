def main():
    filename = "marks.txt"

    print("Total number of students: ")
    n = int(input())

    # Write student data to marks.txt
    f = open(filename, "w")
    for i in range(n):
        print("Enter student name:")
        name = input()
        print("Enter marks:")
        marks = input()
        f.write(name + " " + marks + "\n")

    f.close()

    # Read and display students with marks > 75
    print("\nStudents with marks more than 75:")
    f = open("marks.txt", "r")

    for line in f:
         name, marks = line.strip().split()
         marks = int(marks)
         if marks > 75:
            print(name, ":", marks)

    f.close()

if __name__ == "__main__":
    main()
