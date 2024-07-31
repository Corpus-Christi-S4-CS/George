import time

while True:

    print("\tLIGHT 1\tLIGHT 2")

    for x in range(1,6):

        print(str(x) + "\tGREEN\tRED")
        time.sleep(1)

    print("6\tORANGE\tRED")
    time.sleep(1)
    
    print("\tLIGHT 1\tLIGHT 2")

    for x in range(1,3):

        print(str(x) + "\tRED\tGREEN")
        time.sleep(1)

    print("3\tRED\tORANGE")
    time.sleep(1)