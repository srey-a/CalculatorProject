from tkinter import *

window=Tk()
window.geometry("280x400")
window.title("CALCULATOR")
window.configure(bg="#669999")

def hello():
    print("button clicked")

button1=Button(window,text="ok",command=hello)
button2=Button(window,text="ok",command=hello)

button1.grid(row=0,column=0)
button2.grid(row=1,column=0)



window.mainloop()

