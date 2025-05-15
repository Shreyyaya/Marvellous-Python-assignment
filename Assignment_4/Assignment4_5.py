from functools import reduce

def CheckPrime(n):
    if n==0 or n==1:
        return False   #as 0 and 1 are neither prime not composite
    for i in range(2, int(n**0.5) + 1):   #loop checks the factors of n from 2 to sqrt(n)
        if n % i == 0:
            return False  #if n is divisible by i ie remainder = 0 then it is not prime 
    return True

def Multiply(no):
    return no*2    #multiplies all the filtered values with 2

def Max(A, B):
    return A if A > B else B  #finds the maximum among mapped outputs anf reduced result

Data = [2,70,11,10,17,23,31,77]
print("Input :", Data)

FData = list(filter(CheckPrime, Data)) 
print("Filter output: ", FData)

MData = list(map(Multiply, FData))
print("Map output: ", MData)

RData = reduce(Max, MData)
print("Reduce output: ", RData)