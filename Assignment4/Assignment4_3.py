from functools import reduce

Greater = lambda no : (no>=70 and no<=90)   #filters data values which are in between 70 and 90

Increase = lambda no : (no+10)  #increases the filter values by 10

Sum = lambda A,B : (A*B)  #multiplies the mapped values

Data = [4,34,36,76,68,24,89,23,86,90,45,70]
print("Input :", Data)

FData = list(filter(Greater, Data)) 
print("Filter output: ", FData)

MData = list(map(Increase, FData))
print("Map output: ", MData)

RData = reduce(Sum, MData)
print("Reduce output: ", RData)