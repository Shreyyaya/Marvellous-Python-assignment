from functools import reduce

CheckEven = lambda no : (no%2 ==0)   #filters out all the even inputs

Square = lambda no : (no**2)  #squares all filtered outputs

Sum = lambda A,B : (A+B)  #adds all the mapped outputs and gives the result

Data = [5,2,3,4,3,4,1,2,8,10]
print("Input :", Data)

FData = list(filter(CheckEven, Data)) 
print("Filter output: ", FData)

MData = list(map(Square, FData))
print("Map output: ", MData)

RData = reduce(Sum, MData)
print("Reduce output: ", RData)