
class Numbers:

    class Arithmetic:    #arithmetic class inside numbers
        def __init__(self, value):
            self.value = value   #value as instance variable

        def Display(self):
            print("The value is:", self.value) #to display the value

        def ChkPrime(self):
            n = self.value
            if n==0 or n==1:
                return False   #as 0 and 1 are neither prime not composite
            for i in range(2, int(n**0.5) + 1):   #loop checks the factors of n from 2 to sqrt(n)
                if n % i == 0:
                    return False  #if n is divisible by i ie remainder = 0 then it is not prime 
            return True 

        def Factors(self):
            print("Factors of entered value (excluding itself): ", end="")
            for i in range(1, self.value):   #range from 1 to entered value
                if self.value % i == 0:
                    print(i, end=" ")   #if the value gets divided by i print
            print()

        def sumFactors(self):
            sum = 0   #sum initialised at 0
            for i in range(1, self.value):
                if self.value % i == 0:    #if the value gets divided add to the sum
                    sum = sum+ i
            return sum

        def chkPerfect(self):
            total = self.sumFactors()   #helper method sumFactors
            if total == self.value:     #if the total sum is same as the value then it is a perfect number
                print("Value is a perfect number")
                return True
            else:
                print("Value is not a perfect number")
                return False


def main():
    val = int(input("Enter a number: "))
    obj = Numbers.Arithmetic(val) 
    obj.Display()
    obj.ChkPrime()
    obj.Factors()
    print("Sum of factors:", obj.sumFactors())
    obj.chkPerfect()


if __name__ == "__main__":
    main()
