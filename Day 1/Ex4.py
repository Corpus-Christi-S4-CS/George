char = str(input("Enter the character(s) you want the pattern to be made out of: "))

num = int(input("Enter how many digits long the pattern should be: "))

for x in range(1,num):

    print(char * x)

for x in range(2,num):

    print(char * (num - x))