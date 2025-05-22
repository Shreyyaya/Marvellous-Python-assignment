i = 1  #global var

def fun(no, count):    #2 parameters are defined so that loop will start from count and goes till no
    global i     #global var i 
    if count <= no:    # if count is either equal or less than no print the i 
        print(i, end ="")
        i = i + 1     #i increment (canges the value of global i)
        fun(no, count + 1)   #recursive call

def main():
    count = int(input("enter the starting number: ")) 
    no = int(input("enter the ending number: "))
    ret = fun(no,count)

if __name__ == "__main__":
    main()
