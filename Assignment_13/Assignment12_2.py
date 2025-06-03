class Circle:
    PI = 3.14   

    def __init__(self, A):   #inside method
        print("Inside Circle constructor")

        self.Radius = A    #instance variable radius is defined

    def CalculateArea(self):   #instance method CalculateArea
        Ans = 0.0 
        Ans = Circle.PI * self.Radius * self.Radius   #formula
        return Ans

class CircleX(Circle):     #single level inheritance
    def __init__(self, A):
        print("Inside CircleX constructor")
        super().__init__(A)  

    def CalculateCircumference(self) :   #instance method CaluculateCircumference
        Ans = 0.0
        Ans= 2 * Circle.PI * self.Radius #fromula
        return Ans  


def Display():
    obj1 = CircleX(float(input("Enter your radius:")))   #user defined radius

    ret = obj1.CalculateArea()
    print("Area of circle is: ", ret)

    ret = obj1.CalculateCircumference()
    print("Circumference of circle is: ", ret)

def main():
    Display()    

if __name__ == "__main__":
    main()    