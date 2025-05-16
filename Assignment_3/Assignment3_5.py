from MarvellousNum import ChkPrime

def ListPrime():
    print("Enter how many elements :")
    size = int(input())

    Data = []
    print("Enter the values: ")


    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered elements are:", Data)


    sum = 0
    for value in Data:
        if ChkPrime(value):
            sum += value

    print("Addition of all prime numbers is:", sum)

if __name__ == "__main__":
    ListPrime()

 
