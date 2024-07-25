def converter(kmph):

    result = kmph * 0.621371
    result = round(result)

    return result

ans4 = int(input("Enter a speed in kilometers per hour: "))

print("The speed in miles per hour is " + str(converter(ans4)) + " to the nearest whole number.")