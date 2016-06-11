######################################################################
# FILE: ithElementValue.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find the number on x position in Fibonacci series
#######################################################################

#The numbers before the current, and that before it. Starting with 1, 1
pre_Num = 1
pre_Pre_Num = 1

orc_Num = int(input("Which Orc do you wish to confront?"))

for i in range(orc_Num - 2):
    # Find the new number of arrows for each orc until the
    # orc we want to confront
    new_Num = pre_Num + pre_Pre_Num
    pre_Pre_Num = pre_Num
    pre_Num = new_Num

print("The required number of arrows is", pre_Num)
