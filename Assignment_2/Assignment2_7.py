print("Enter a number: ")
n = int(input())

for x in range(n):
    for i in range(1, n + 1):  #starts from 1 till n-1
        print(i, end = "")  #end statemnt so that output will display on same line
    print()