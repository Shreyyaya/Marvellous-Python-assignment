def Factorial(i):
    if i == 0 or i == 1:   #the factorial of 0 and 1 is 1 itself
        return 1
    
    else:
        return i * Factorial(i - 1)   #formula for factorial 


if __name__ == "__main__":
    
    print("Enter the number:")
    value = int(input())

    print("Factorial of the number is :")
    print(Factorial(value))

