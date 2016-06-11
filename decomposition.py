######################################################################
# FILE: decomposition.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find the number of goblets Gimli drank of each day
#######################################################################

num_Of_Goblets = int(input("Insert composed number:"))
num_Of_Days = 1
DECIMAL_BASE = 10

if num_Of_Goblets == 0:
    #Gimli has not drank nothing
    print("The number of goblets Gimli drank on day", num_Of_Days, "was",\
    num_Of_Goblets)

while num_Of_Goblets != 0:
    #Check whats the last digit and prints with the current day
    last_Digit = num_Of_Goblets % 10
    print("The number of goblets Gimli drank on day", num_Of_Days, "was",\
    last_Digit)
    
    #Change for next day and divide (integer) the number by 10
    num_Of_Days += 1
    num_Of_Goblets //= DECIMAL_BASE
