######################################################################
# FILE: binaryToDecimal.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Convert a number from binary to decimal base
#######################################################################

binary = int(input("Insert number in binary representation:"))
counter = 0
decimal = 0
DECIMAL_BASE = 10
BINARY_BASE = 2

#This algorithm is based on the method learned in class for converting
#decimal number to binary number. It takes the binary number entered, modolu
#it by 19, takes the result, multiply it by 2**counter (counter is the number
#of times the while loop runs) and add the result to the decimal variable.
#Then is divides the binary number by 10. The whole loop repeats itself until
#the binary variable is 0
while binary != 0:
    decimal += (binary%DECIMAL_BASE)*(BINARY_BASE**counter)
    binary //= DECIMAL_BASE
    counter += 1

print("The decimal value of the inserted binary number is", decimal)

