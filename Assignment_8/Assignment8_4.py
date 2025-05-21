import threading

def small(s):   #function for lower case letters
    count = 0
    for c in s:
        if c.islower():    #islower() is a function that detects letters in lower case
            count = count+ 1

    print("Number of small letters:", count)

def capital(l):    #function for upper case letters
    count = 0
    for c in l:
        if c.isupper():   #isupper() is a function that detects letters in upper case
            count = count + 1
    print("Number of capital letters:", count)


def digits(d):    #displays total length of the string
    print("Length of the string:", len(d))

def main():
    print("Enter the string: ")   #user defined input
    str = input()

    T1 = threading.Thread(target=small, args=(str,))
    T2 = threading.Thread(target=capital, args=(str,))
    T3 = threading.Thread(target=digits, args=(str,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("end of main")

if __name__ == "__main__":
    main()
