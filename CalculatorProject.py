#Calculatorproject using Tkinder

#import everything from tkinder module

from tkinter import *

expression=""  #globally declare the expression variable

def press(num):   #in the text entry box

    global expression

    expression=expression+str(num)   #concatenation of the string

    equation.set(expression)   #function to evaluate by using set method