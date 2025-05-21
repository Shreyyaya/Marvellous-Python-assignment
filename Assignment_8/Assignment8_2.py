import threading
import os

def evenfactor(n):
    print("PID of evenfactor is:", os.getpid())
    even_sum = 0     #sum is initialized as 0
    for i in range(2,n + 1, 2):  
        if n % i == 0:  #if the number in the factors get divided by 2 then do +i in even_sum
            even_sum = even_sum + i
    print("Sum of even factors:", even_sum)

def oddfactor(n):
    print("PID of oddfactor thread is:", os.getpid())
    sum_odd = 0
    for i in range(1,n + 1, 2):
        if n % i == 0:
            sum_odd = sum_odd+ i
    print("Sum of odd factors:", sum_odd)

def main():
    print("Enter a big number (in millions): ")
    num = int(input())

    print("PID of main process is:", os.getpid())

    T1 = threading.Thread(target=evenfactor, args=(num,))
    T2 = threading.Thread(target=oddfactor, args=(num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__=="__main__":
    main()    
    print("exit from main")
   