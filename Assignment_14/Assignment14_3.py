class Book:
    def __init__(self, A, B):
        self.Name = A       #public with 0 underscore
        self.__Price = B    #private with 2 underscore

    def getPrice(self):
        return self.__Price   #get method to get the price
    
    def setPrice(self, value):
        if value >= 0: 
            self.__Price = value    #set method to set the price


obj = Book("C programming", 250)        

print("Book name:", obj.Name)
print("Book price:", obj.getPrice())

