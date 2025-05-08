def Add(no1, no2):     #Add function id defined which accepts 2 parameters
    result = no1 + no2   #result gives us addition of the accepted parameters
    return result

print("Enter first number:")
no1 = int(input())

print("Enter second number:")
no2 = int(input())

ans = Add(no1,no2)     #Add function is used to add the accepted integers from user
print("The addition is:", ans)
