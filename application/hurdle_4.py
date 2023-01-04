# --- Defining the "turn_right" Function ---
def turn_right(a, b):
    for c in range(a, b):
        turn_left()
  

def wall_on_left():
    while not wall_in_front():
        move()
    
    
# --- Defining the Movements ---
def movements():    
    turn_right(0, 3)
    move()
    turn_right(0, 3)
    wall_on_left()
    turn_right(0, 1)

            
# --- MAINLY PROGRAM ---
while not at_goal():
    if wall_in_front() == True:
        turn_left()
        while wall_on_right() :
            move()
        movements()
    else:
        move()



    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
