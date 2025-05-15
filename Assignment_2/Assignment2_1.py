#importing module arithmatic to perform the operation on user defined inputs

from Arithmatic import Add, Sub, Mul, Div

def main():

    print("enter First number: ")   #user defined input
    no1 = int(input())

    print("enter Second number: ")  #user defined input
    no2 = int(input())

    Result = Add(no1, no2)
    print ("The Addition is: ", Result)

    Result = Sub(no1, no2)
    print ("The Substraction is: ", Result)


    Result = Mul(no1, no2)
    print ("The Multiplication is: ", Result)

 
    Result = Div(no1, no2)
    print ("The Division is: ", Result)
    

if __name__ == "__main__":
    main()    