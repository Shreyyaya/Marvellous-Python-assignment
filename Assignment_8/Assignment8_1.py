import threading 
import time
import os


def Even():
    print("PID of SumEven process is: ", os.getpid())
    
    for i in range (2,21,2):    #range is between 2 and 21 and dsplacement is 2 to display first 10 even numbers
        print(i)
    time.sleep(1)     #to cause 1 sec delay in between execution of 2 threads


def Odd():
    print("PID of SumOdd Process is: ",os.getpid())

    for i in range (1,20,2):     #range is between 1 and 20 and dsplacement is 2 to display first 10 odd numbers
        print(i)    

def main():

    print("PID of main process is: ", os.getpid())

    T1 = threading.Thread(target = Even)

    T2 = threading.Thread(target = Odd)

    T1.start()
    T1.join()   #join is written immediately after the initialization of thread1 so that the execution dont get interrupted by thread2 

    T2.start()
    T2.join()


    print("End of main")

if __name__=="__main__":
    main()    
   