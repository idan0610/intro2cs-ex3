######################################################################
# FILE: twoDimensionalSeek.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex3 2014-2015
# DESCRIPTION:
# Find direct route to destination
#######################################################################
import math

move_x = 0 # Whats the position on x-axis
move_y = 0 # Whats the position on y-axis
is_Right = True # Last move was right?
is_Up = True # Last move was up?
counter = 0 # How many moves, to check which axis they move now

current_turn = input("Next turn:")

while current_turn != "end":
    steps = int(input("How many steps?"))
    
    if counter % 2 == 0:
        #Move on x-axis
        if is_Up:
            #Last move was north
            if current_turn == "right":
                #Move east
                move_x += steps
                is_Right = True
            else:
                #Move west
                move_x -= steps
                is_Right = False
        else:
            #Last move was south
            if current_turn == "right":
                #Move west
                move_x -= steps
                is_Right = False
            else:
                #Move east
                move_x += steps
                is_Right = True
    else:
        #Move on y-axis
        if is_Right:
            #Last move was east
            if current_turn == "right":
                #Move south
                move_y -= steps
                is_Up = False
            else:
                #Move north
                move_y += steps
                is_Up = True
        else:
            #Last move was west
            if current_turn == "right":
                #Move north
                move_y += steps
                is_Up = True
            else:
                #Move south
                move_y -= steps
                is_Up = False

    
    counter += 1
    current_turn = input("Next turn:")

#Check if east or west from initial position
if move_x >= 0:
    turn_x = "right"
else:
    turn_x = "left"

#Check if north or south from initial position
if move_y >= 0:
    turn_y = "forward"
else:
    turn_y = "backward"

#Where Gandalf should move on eagle?
print("Gandalf should fly", int(math.fabs(move_x)), "steps", turn_x, \
"and", int(math.fabs(move_y)), "steps", turn_y)
