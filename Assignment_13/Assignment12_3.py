class Arithematic:

    def __init__(self, Value1=0, Value2=0):    #instance method with variavles value1 and value 2 initialized at 0
        print("Inside constructor")
        self.no1 = Value1
        self.no2 = Value2

    def __del__(self):
        print("Inside destructor")
        
    def Accept(self):  
        self.no1 = int(input("Enter first number: "))      #user defined inputs
        self.no2 = int(input("Enter second number: ")) 

    def Addition(self):
        return self.no1 + self.no2   #instance methods

    def Substraction(self):
        return self.no1 - self.no2      

    def Multiplication(self):
        return self.no1 * self.no2
    
    def Division(self):
        return self.no1 / self.no2


def main():
    obj = Arithematic()  
    obj.Accept()          # takes user inputs

    print("Addition:", obj.Addition())   
    print("Subtraction:", obj.Substraction())
    print("Multiplication:", obj.Multiplication())
    print("Division:", obj.Division())


if __name__ == "__main__":
    main()
