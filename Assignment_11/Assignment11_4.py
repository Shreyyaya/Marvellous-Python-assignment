
def Power(no, count):
    if no == 0 and count == 0:
        return "undefined"  # 0 p0wer 0 is mathematically undefined
    elif count == 0:
        return 1   #any number power 0 always gives 1
    else:
        return no ** count  #no^count

def main():
    no = int(input("Enter the base number: "))
    count = int(input("Enter the power number: "))
    ret = Power(no, count)
    print("power is:", ret)

if __name__ == "__main__":
    main()
