######################################################################
# FILE: totalWeight.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find the total weight
#######################################################################

print("Insert weights one by one:")

# reset total and ask for first input
RING_WEIGHT = -1.0
MAX_WEIGHT = 100.0
total = 0
current = float(input())

while current != RING_WEIGHT:
    #runs until the user input -1
    if current != -1.0 and current < 0.0:
        #if the current input is negative but not -1, print error and continue
        print("Weights must be non-negative")
        current = float(input())
        continue
    
    total += current
    
    if total > MAX_WEIGHT:
            #if the total bigger then 100, print error and break
            print("Overweight! Gandalf will not approve.")
            break;
    
    current = float(input())
    
if total <= MAX_WEIGHT:
    #print only if not overweight
    print("The total packed weight is", total)
