
def Num():
    print("enter the number:")
    number = int(input())    #number parameter accepts user value in integer datatype

    if(number%5==0):     # if the number accepted gives 0 remainder value when divided by 5 then True gets printed
        print("True")

    else:
        print("False")

if __name__ =="__main__":
    Num()



