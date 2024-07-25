def converter(temp):
    kelvin = temp + 273.15
    return kelvin

userTemp = float(input("Enter the temperature in celsius: "))

print("The temperature in kelvin is " + str(converter(userTemp)) + ".")