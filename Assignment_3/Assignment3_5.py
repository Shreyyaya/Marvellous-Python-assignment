from MarvellousNum import ChkPrime   #chkPrime function imported from MarvellousNum module

def ListPrime():
    print("Enter how many elements :")
    size = int(input())     

    Data = []
    print("Enter the values: ")


    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered elements are:", Data)


    sum = 0   #sum initialized from 0
    for value in Data:
        if ChkPrime(value):   
            sum += value    #gives summation of all prime numbers given as input

    print("Addition of all prime numbers is:", sum)

if __name__ == "__main__":
    ListPrime()

 
