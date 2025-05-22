
no = 1

def Pattern(n, count):   # 2 parameters are taken
    global no   #global var

    if count > n: 
        return print('*' * count) #loop goes till count > n 

    Pattern(n, count + 1)  #recursive call wiith count+1

def main():
    n = int(input("Enter number of rows: "))
    Pattern(n, no)

if __name__ == "__main__":
    main()
