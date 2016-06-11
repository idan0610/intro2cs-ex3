######################################################################
# FILE: binaryToDecimal.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Convert a number from binary to decimal base
#######################################################################

decimal = int(input("Insert number in decimal representation:"))
counter = 0
binary = 0
DECIMAL_BASE = 10
BINARY_BASE = 2

#This algorithm is the same as the one in binaryToDecimal.py, with decimal and
#bianry bases switched. It takes the decimal number entered, modolu it by 2,
#takes the result, multiply it by 10**counter (counter is the number of times
#the while loop runs) and add the result to the binary variable.
#Then is divides the decimal number by 2. The whole loop repeats itself until
#the decimal variable is 0
while decimal != 0:
    binary += (decimal%BINARY_BASE)*(DECIMAL_BASE**counter)
    decimal //= BINARY_BASE
    counter += 1
    
print("The binary value of the inserted decimal number is", binary)
