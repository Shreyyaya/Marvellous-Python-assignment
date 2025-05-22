
def Zero(no):

    if no == 0:
        return 1   #if number entered is 0 it default has 1 zero
    
    count = 0
    while no > 0: 
        if no % 10 == 0:  #if the modulus of number with 10 is zero then do count+1
            count = count+ 1
        no = no // 10   #apply floor division to find out rest of the numbers
    return count

def main():
    no = int(input("Enter a number: "))
    print("Number of zeros:", Zero(no))

if __name__ == "__main__":
    main()
