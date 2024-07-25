def primeCheck(num):

    prime = True
    x = 2

    if num == 1:

        prime = False

    while prime == True and x < num:

        check = num % x

        if check == 0:
            
            prime = False
        
        x = x + 1
    
    return(prime)

ans5 = int(input("Enter a number: "))

if primeCheck(ans5) == True:
    print(str(ans5) + " is a prime number.")
else:
    print(str(ans5) + " is not a prime number.")