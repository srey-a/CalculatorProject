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

if __name__ == "__main__":  #create a GUI window

    gui = Tk()

    gui.configure(background="#EBEEF3")   #set the background colour of GUI window

    gui.title("Simple Calculator")   #set the title of GUI window

    gui.geometry("285x400")   #set the configuration of GUI window

    equation = StringVar()    #create the text entry box for showing the expression

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=75,ipady=25,padx=4,pady=10)

    equation.set('enter your expression')

    #create a button and place at a particular location
    #when the button press,the action is executed

    button1 = Button(gui, text=' 1 ', fg='black', bg="#669999",
                     command=lambda: press(1), height=4, width=7, bd=5)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg="#669999",
                     command=lambda: press(2), height=4, width=7, bd=5)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg="#669999",
                     command=lambda: press(3), height=4, width=7, bd=5)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg="#669999",
                     command=lambda: press(4), height=4, width=7, bd=5)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg="#669999",
                     command=lambda: press(5), height=4, width=7, bd=5)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg="#669999",
                     command=lambda: press(6), height=4, width=7, bd=5)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg="#669999",
                     command=lambda: press(7), height=4, width=7, bd=5)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg="#669999",
                     command=lambda: press(8), height=4, width=7, bd=5)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg="#669999",
                     command=lambda: press(9), height=4, width=7, bd=5)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg="#669999",
                     command=lambda: press(0), height=4, width=7, bd=5)
    button0.grid(row=5, column=0)


    plus = Button(gui, text=' + ', fg='black', bg="#669999",
                  command=lambda: press("+"), height=4, width=7,bd=5)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg="#669999",
                   command=lambda: press("-"), height=4, width=7,bd=5)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg="#669999",
                      command=lambda: press("*"), height=4, width=7,bd=5)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg="#669999",
                    command=lambda: press("/"), height=4, width=7,bd=5)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg="#669999",
                   command=equalpress, height=4, width=7,bd=5)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg="#669999",
                   command=clear, height=4, width=7,bd=5)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()


