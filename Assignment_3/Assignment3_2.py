
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

    add = 0
    Result = max(Data)  
    print("Maximum value is: ", Result)


if __name__ == "__main__":
    main()   