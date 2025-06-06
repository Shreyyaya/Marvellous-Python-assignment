
class Rectangle:

    def __init__(self, A, B):
        print("Inside rectangle constructor")

        self.Length = A
        self.Width = B    #rectangle is a base class


    def CalculateArea(self):
        Ans = 0.0
        Ans = self.Length * self.Width
        return Ans

class RectangleX(Rectangle):  
    def __init__(self, A, B):
        print("Inside RectangleX constructor")
        super().__init__(A, B)    #rectangleX is a derived class


    def CalculatePerimeter(self) :
        Ans = 0.0
        Ans= 2 * (self.Length + self.Width) 
        return Ans  


def main():
    obj = RectangleX(10, 5) 
    ret = obj.CalculateArea()
    print("Area of rectangle is: ", ret)
    ret = obj.CalculatePerimeter()
    print("Perimeter of rectangle is: ", ret)


if __name__ == "__main__":
    main()    