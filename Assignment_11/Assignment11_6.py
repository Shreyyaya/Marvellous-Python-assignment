
sum = 0 #global var set to 0

def Add(no):
    global sum  

    if(no>=1):
        sum = sum + no
        no = no-1
        Add(no)   #recursive call

    return sum
 

def main():
    ret = Add(int(input("Enter a number: ")))
    print("Sum_n is: ", ret)

if __name__ == "__main__":
    main()    