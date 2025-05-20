import os
import multiprocessing

def Factorial(no):   #function for factorial
    fact = 1

    while(no>=1):
        fact = fact * no
        no = no - 1 

    return fact  


def main():
    data = [120, 250, 360]   #data is given
    result = []


    p = multiprocessing.Pool()   #grouping of processors is done
    result = p.map(Factorial, data)  
    
    p.close()
    p.join()

    print(result)



if __name__ == "__main__":
    main()    
