import time
from Pong import PongGame

# Initialize the game
mygame = PongGame()


"""
    White Button - 1 player mode
    Yellow Button - 2 player mode 
"""
# Main game loop
try:
    while True:
        time.sleep(0.1)  # Small delay to avoid busy-waiting
        # The button press handlers will be triggered by the Button class
        print("Main loop iteration.")  # Add a print statement to indicate the loop is running

except KeyboardInterrupt:
    print("Game interrupted.")
finally:
    # Clean up if necessary
    pass
