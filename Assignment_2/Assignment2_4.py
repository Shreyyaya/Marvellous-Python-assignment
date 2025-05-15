def Fact_sum(n):
    total = 0
    for i in range(1, n):    #range of i is defined from 1 to n-1
        if n % i == 0:   #checks if i is an factor of n or not
            total += i    #if i is a factor it gets added to total
    return total

print("Enter a positive integer:")
num = int(input())

result = Fact_sum(num)
print("Sum of proper factors of", num, "is:", result)
