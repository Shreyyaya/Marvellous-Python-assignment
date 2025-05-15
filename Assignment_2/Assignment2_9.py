print("Enter a number: ")
num = int(input())
num_len = len(str(num))   #we can't directly apply len function to int so type casting
print("Number of digits:", num_len)
