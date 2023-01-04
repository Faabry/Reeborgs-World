# --- Defining the "turn_right" Function ---
def turn_right(a, b):
    for c in range(a, b):
        turn_left()

# --- Defining a special condition ---
while front_is_clear():
    move()
turn_left()

# --- MAINLY PROGRAM ---
while not at_goal():
    if right_is_clear():       
        turn_right(0, 3)
        move()    
    elif front_is_clear():
        move()
    else:
        turn_left()
        



    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
