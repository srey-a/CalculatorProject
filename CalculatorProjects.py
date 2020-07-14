#Calculatorproject using Tkinder

#import everything from tkinder module
from tkinter import  *

#globally declare the expression variable
expression=""

#in the text entry box
def press(num):

    global expression

    expression=expression+str(num) #concatenation of string

    equation.set(expression)       #function to evaluate the final expression

def equalpress():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""           #initialise the expression variable

    except:

        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

    