import multiprocessing  
import os



def evenlist(no):
    print("PID of evenlist process is: ", os.getpid())
    sum = 0
    for i in range(2,no+1,2):  #returns sum of even numbers
        sum = sum + i

    print(sum)

def oddlist(no):
    print("PID of oddlist Process is: ",os.getpid())
    sum = 0
    for i in range(1,no+1,2):   #returns sum of odd numbers
        sum = sum + i

    print(sum)    

def main():

    T1 = multiprocessing.Process(target = evenlist, args=(800000000, ))
    T2 = multiprocessing.Process(target = oddlist, args=(700000000, ))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("End of main")

if __name__=="__main__":
    main()    
   