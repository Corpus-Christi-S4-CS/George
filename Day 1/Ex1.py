import random

temp = random.randint(20,26)
print(temp)

if temp < 22:
    
    print("Cold")

elif temp >= 22 and temp <= 24:
    
    print("Warm")

elif temp > 24:

    print("Hot")