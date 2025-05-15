print("Enter a number: ")
x = int(input())

for i in range(1, x + 1):  #x+1 cause we want the output till x
    for j in range(1, i + 1):  #2nd loop to print the ouput in row and column format
        print(j, end='') 
    print()
