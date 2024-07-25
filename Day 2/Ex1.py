def calculation(num1,num2):
    
    result = (num1 + num2) * 10
    
    return result

ans1 = int(input("Enter a number: "))
ans2 = int(input("Enter another number: "))

print("The result of the calculation is " + str(calculation(ans1, ans2)))