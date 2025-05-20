import threading  
import time

def Display():
    print("Inside display")
    for i in range(1,6):    #range is set from 1 to 5 
        print(i)
    time.sleep(1)    


def main():
    print("Inside main")
    T1 = threading.Thread(target = Display)   #thread 1 initialize
    T1.start()   
    T1.join()
    T2 = threading.Thread(target = Display)   #thread 2 initialize
    T2.start()   
    T2.join()
    T2 = threading.Thread(target = Display)   #thread 3 initialize
    T2.start()   
    T2.join()
    print("End of main")  
    

if __name__=="__main__":
    main()    