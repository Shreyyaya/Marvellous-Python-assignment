class Employee:
    def __init__(self, A, B, C):
        self.Name = A       #public with 0 underscore
        self._Dept = B       #protected with 1 underscore
        self.__Salary = C    #private with 2 underscore


    def Display(self):
        print(self.Name)
        print(self._Dept)
        print(self.__Salary)


obj = Employee("Rohit", "CSE" , 50000)        

obj.Display()

print(obj.Name)
print(obj._Dept)
#print(obj.__Salary)  we can't access private variable
