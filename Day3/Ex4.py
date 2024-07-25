array = [12, 76, 3, 4, 35, 2, 10, 8]

sorted = False

while sorted == False:

    sorted = True

    for x in range(len(array) - 1):
    
        if array[x] > array[x + 1]:

            num = array[x + 1]
            array[x + 1] = array[x]
            array[x] = num
            sorted = False

print(array)