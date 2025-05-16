
def main():
    print("Enter how many elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered elements are: ") 
    print(Data)     
    print()

    add = 0
    Result = min(Data)  
    print("Minimum value is: ", Result)  #min function is defined to pick out the minimum number from the list


if __name__ == "__main__":
    main()   
