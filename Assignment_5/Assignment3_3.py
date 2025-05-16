
def Frequency(data, target):
    count = 0
    for num in data:
        if num == target:
            count += 1
    return count


def main():
    print("Enter how many elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered elements are: ") 
    for value in Data:
        print([value], end ="")       
    print()

    print("Enter the number to search for frequency:")
    search = int(input())
    freq = Frequency(Data, search)
    print("Frequency of that number is: ", freq)



if __name__ == "__main__":
    main()   