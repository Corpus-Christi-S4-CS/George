def factorial(num):

    result = num

    while num != 1:

        num = num - 1
        result = result * num

    return result

ans = int(input("Enter a number: "))

print("The factorial is " + str(factorial(ans)))