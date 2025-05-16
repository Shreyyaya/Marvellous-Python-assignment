def Frequency(data, target):     #frequency function is defined with 2 parameters 
    count = 0  #initialized count as 0
    for num in data:
        if num == target:   #if the number entered for search matches the target then count gets updated
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
    print(Data)     
    print()

    print("Enter the number to search for frequency:")
    search = int(input())   #input is taken from user to check its frequency
    freq = Frequency(Data, search)  
    print("Frequency of that number is:", freq)

if __name__ == "__main__":
    main()
