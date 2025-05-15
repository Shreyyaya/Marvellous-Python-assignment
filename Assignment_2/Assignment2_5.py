
print("Enter a number: ")
num = int(input())

if num == 0 or num == 1:   #0 and 1 are neither composite or prime
    print(num, "is not a prime number")

elif num > 1:
    for i in range(2, num):  #range starts from 2 to input 
        if (num % i) == 0:   #checks if i is a factor of input or not
            print(num, "is not a prime number")
            break  #to avoid looping
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
