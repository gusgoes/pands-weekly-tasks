#asks the user to input any positive integer and outputs the successive values of the following calculation.

num = int(input("Insert any positive integer number: "))
numbers = []

#At each step calculate the next value by taking the current value and, 
#if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.
if  (num==1):
    numbers.append(num)
    print (numbers)
else:
    while (num!=1):
        if (num%2 == 0):
            num = int(num/2)
            numbers.append(num)
        else:
            num = int((num*3)+1)
            numbers.append(num)
    print (numbers)