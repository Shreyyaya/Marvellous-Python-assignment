import os
import threading 
import multiprocessing
import time

def Add(no):       #a common function is defined to do the sum of numbers from 1 to 10 million
    sum = 0 
    for i in range(1, 10000001):  
        sum = sum + i
    return sum    

def Target(result):   #target function for multithreading
    result[0] = Add(0)

def Function():          #to calculate the time using normal def function
    start = time.time()    #time module is used to start the time
    result = Add(0)
    end = time.time() 

    print("Function Result:", result)
    print("Normal Time:", end - start, "seconds")   #displays the execution time using normal function
    print()


def Thread():
    result = [0]

    def Target():       #a nested function is used to define the target
        result[0] = Add(0)

    t = threading.Thread(target=Target)  #thread is initialized

    start = time.time()
    t.start()
    t.join()
    end = time.time()

    print("Threading Result:", result[0])
    print("Threading Time:", end - start, "seconds")    #displays the execution time using threading
    print()

def Multiprocessing():
    start = time.time()
    with multiprocessing.Pool() as p: 
        result = p.map(Add, [0]) 
    end = time.time()

    print("Multiprocessing Result:", result[0])
    print("Multiprocessing Time:", end - start, "seconds")    #displays the execution time using multiprocessing
    print()

if __name__ == "__main__":
    print("Comparing normal function vs threading vs multiprocessing:")
    print()
    Function()
    Thread()
    Multiprocessing()       
