#Calculatorproject using Tkinder

#import everything from tkinder module

from tkinter import *

expression = ""  #globally declare the expression variable

def press(num):  #in the text entry box

    global expression

    expression = expression + str(num)   #concatenation of string

    equation.set(expression)      #function to evaluate by using set method

def equalpress():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:             #by the expect block

        equation.set(" error ")
        expression = ""

def clear():         #function to clear the content
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="#EBEEF3")

    gui.title("Simple Calculator")

    gui.geometry("285x400")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=75,ipady=25,padx=4,pady=10)

    equation.set('enter your expression')

