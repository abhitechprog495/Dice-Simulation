#-------------------------------------------------------------------------------
# Name: Dice Simulation
# Purpose: To understand the randomness
# Author: Abhishek Kumar
#-------------------------------------------------------------------------------
# Importing necessary libraries, modules and packages

import tkinter
from PIL import Image, ImageTk
import random

# Main window

root =  tkinter.Tk()
root.geometry('500x500')
root.title("Roll the Dice")

# Images of dice of different number faces

dice_image = ['images\dice1.jpg', 'images\dice2.jpg', 'images\dice3.jpg', 'images\dice4.jpg', 'images\dice5.jpg', 'images\dice6.jpg']

# Simulating the dice images with random numbers between 0 to 6

image_of_dice = ImageTk.PhotoImage(Image.open(random.choice(dice_image)))

# Widget for image

image_label = tkinter.Label(root, image=image_of_dice)
image_label.image = image_of_dice

# Pack the image widget into the parent widget
image_label.pack(expand=True)

# Function for button click
def rolling_dice():
    image_of_dice = ImageTk.PhotoImage(Image.open(random.choice(dice_image)))
    # Update the image of dice
    image_label.configure(image=image_of_dice)
    image_label.image = image_of_dice

# Adding button for simulation of dice

button = tkinter.Button(root, text='Roll the Dice', fg='red', command=rolling_dice)

# Pack the button widget into the parent widget

button.pack(expand=True)

# Start the main window and keep it active

root.mainloop()
