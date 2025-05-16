def ChkPrime(num):       #module that contains a function to check whether the number is prime or not
    if (num ==0 or num==1):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
