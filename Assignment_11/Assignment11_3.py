
def Add(no):
    if no > 0:
        return (no % 10) + Add(no // 10)   #when the user defined output is taken, firstly modulus with 10 is taken to find out the last digit and then
                                           # floor division is done to find out rest of the number and is recurcively done until we get the whole input  
                                           #eg. 15 = at first modulus with 10 is done to find out 5 is at the unit place, then floor division is done
                                           #to find out 1 is at the 10th place
    else:
       return 0
    

def main():
    ret = Add(int(input("Enter a number: ")))
    print("Sum_of_digits is:", ret)

if __name__ == "__main__":
    main()
