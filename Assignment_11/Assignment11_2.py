
def factorial(no):    #function to calculate the factorial
    fact = 1

    while(no>=1):
        fact = fact * no
        no = no - 1 

    return fact    #recursive call
 

def main():
    ret = factorial(int(input("Enter the number: ")))
    print("Factorial is: ", ret)

if __name__ == "__main__":
    main()    