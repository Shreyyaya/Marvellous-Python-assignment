import threading 
import os
import time


def Normal():
    for i in range(1,51):    #function to display 1 to 50 serially
        print(i)
    time.sleep(1)     # 1 sec display delay between thread1 and thread2

def Reverse():
    for i in range(50,0,-1):     #function to display 1 to 50 in reverse
        print(i)    

def main():

    thread1 = threading.Thread(target = Normal)
    thread2 = threading.Thread(target = Reverse)

    thread1.start()
    thread1.join()
    print()

    thread2.start()
    thread2.join()

    print("End of main")

if __name__=="__main__":
    main()    
   