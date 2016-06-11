######################################################################
# FILE: findSecondSmallest.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find the second smallest number
#######################################################################

NUM_OF_DANCERS = 10
minHeight = 0
secMinHeight = 0
minPos = 0
secMinPos = 0

for i in range(NUM_OF_DANCERS):
    #runs 10 times, each time asks for new age
    temp = int(input("What is the age of the current dancer?"))
    
    if i == 0:
        #if runs the first time, put the input in minHeight
        minHeight = temp
    elif i == 1:
        #if runs the second time...
        if temp < minHeight:
            #the input is lower then minHeight
            secMinHeight = minHeight
            minHeight = temp
            minPos = i
            secMinPos = i - 1
        else:
            #the input is larger then minHeight but lower then secMinHeight
            secMinHeight = temp
            secMinPos = i
    elif temp < minHeight:
        #the input is lower then minHeight
        secMinHeight = minHeight
        minHeight = temp
        secMinPos = minPos
        minPos = i
    elif temp < secMinHeight:
        #the input is larger then minHeight but lower then secMinHeight
        secMinHeight = temp
        secMinPos = i

print("Pippin is dancer number", secMinPos+1)
