# --- Defining the "turn_right" Function ---
def turn_right(a, b):
    for c in range(a, b):
        turn_left()
  

# --- Defining the Movements ---
def movements():
    for c in range(0, 6):
        move()
        turn_left()
        move()
        turn_right(0, 3)
        move()
        turn_right(0, 3)
        move()
        turn_right(0, 1)

            
# --- MAINLY PROGRAM ---
movements()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
