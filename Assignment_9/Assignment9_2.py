import os
import multiprocessing


def Square(no):  
    return no**2    #function is defined to sqaure the input value


def main():
    data = [1000000, 2000000, 3000000]   #data is given 
    result = []   #result empty list


    p = multiprocessing.Pool()   #pooling method that groups the processes
    result = p.map(Square, data)   #mapping in parallel is done
    
    p.close()  
    p.join()  

    print(result)



if __name__ == "__main__":
    main()    
