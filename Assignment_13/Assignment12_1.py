class Demo:
    ClassVar = "Value"  #class variable 

    def __init__(self, no1, no2):     #instance method
        self.no1 = int(input("Enter first number: "))    #user defined inputs
        self.no2 = int(input("Enter second number: "))   #instance variable no1, no2 which accepts user defined values ignoring the given input values 


    def Fun(self):
        print("Inside Fun =", self.no1, self.no2)   #instance method fun

    def Gun(self):
        print("Inside Gun =", self.no1, self.no2)   #instance method gun 


def main():
    print("Class variable:", Demo.ClassVar)

    obj1 = Demo(10,11)
    obj2 = Demo(20,21)   #inputs given to fun and gun

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()    #prints user defined values ignoring the given inputs


if __name__ == "__main__":
    main()        