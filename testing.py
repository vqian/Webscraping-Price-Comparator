from tkinter import *
from UserInput import UserInput

def getUserInput(prompt):
    inputBox = UserInput(prompt)
    inputBox.waitForInput()
    return inputBox.getString()

userInput = getUserInput("Please enter item name")
print("User Input:", userInput)