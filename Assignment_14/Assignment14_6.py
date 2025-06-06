class Calculator:

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def add(self):
        return self.no1 + self.no2

    def sub(self):
        return self.no1 - self.no2

    def mul(self):
        return self.no1 * self.no2

    def div(self):
        return self.no1 / self.no2

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))


    calc = Calculator(a, b)

    print("Addition:", calc.add())
    print("Subtraction:", calc.sub())
    print("Multiplication:", calc.mul())
    print("Division:", calc.div())

if __name__ == "__main__":
    main()
    