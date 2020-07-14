#Calculatorproject using Tkinder

#import everything from tkinder module
from tkinter import *

#globally declare the expressin variable
expression=""

#in the text entry box
def press(num):

    global expression

    expression=expression+str(num) #concatenation of string

    equation.set(expression)   #function to evaluate the final expression

