######################################################################
# FILE: findLargest.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find the position of largest number fron n numbers
#######################################################################
#asks the number of runs for the for
num = int(input("Enter the number of riders:"))
maxNum = 0
maxNumPos = 0

for i in range(num):
    temp = int(input("How tall is the hat?"))
    if temp > maxNum:
        #if the input is larger then maxNum
        maxNum = temp
        maxNumPos = i

print("Gandalf's position is:", maxNumPos+1)

