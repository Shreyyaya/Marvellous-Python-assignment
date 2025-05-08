
def ChkNum():     #ChkNum function is defined
    print("enter the number:")  
    number = int(input())     #number parameter accepted as integer

    if(number%2==0):       #if the number results in 0 remainder if divided by 2 then it is even
        print("The number is even")

    else:
        print("The number is odd")

if __name__ =="__main__":  
    ChkNum()




