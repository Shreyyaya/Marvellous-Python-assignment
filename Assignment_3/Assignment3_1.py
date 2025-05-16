
def main():
    print("Enter how many elements :")
    size = int(input())   #user defined inputs

    Data = list()  #empty list is defined

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)  #the inputs gets appended in the empty list named Data

    print("Entered elements are: ") 
    for value in Data:
        print([value], end ="")       
    print()   #entered Numbers gets printed

    add = 0
    Result = sum(Data)  
    print("Addition is: ", Result) #sum function is defined to do the addition of all numbers given as inputs


if __name__ == "__main__":
    main()   
