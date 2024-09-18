'''
Program Name: Console Snake
Program Author: (name)
Date Created: (date)
Description: (1-2 sentences)
'''

import snake
import input
import display
import apples
import time

TICKRATE = 4
inputHandler = input.InputHandler()
inputHandler.start()

def tick():
    """
    tick() runs once per game tick. This is where you should write your code to:

    Move the snake (using your snake class),
    Display the screen (using pre-made display class),
    Handle the snake eating apples (using your apple class),
    Grow the snake (using your snake class),
    Creating new apples,
    Display and deal with the different game states like winning and losing.
    """

    # example usage of InputHandler
    lastKeyPressed = inputHandler.getLastKeyPress() # gets the last key pressed
    # example usage of the Image class
    image = display.Image(11,11,".") # makes a 11x11 image of "."
    image.set((3,4), "#") # sets the pixel (3,4) to "#"
    image.display() # prints the image
    image.fill("!") # fills the image with "!"
    image.display() # displays the new image

    pass

# main loop
while True:
    time.sleep(1 / TICKRATE)
    tick()
