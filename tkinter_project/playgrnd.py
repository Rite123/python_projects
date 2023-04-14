import tkinter
from tkinter import END

screen=tkinter.Tk()
screen.title("This is first Tk")
screen.minsize(width=800,height=400)


label=tkinter.Label(text="FUNCTION" , font=("consoles",16))
label.grid(row=4,column=1)

def button_click():
    name=input_.get()
    label["text"] = name

button=tkinter.Button(text="Click",command=button_click)
button.grid(row=3,column=2)

input_ = tkinter.Entry(width=10,font=("times new roman",14))
input_.insert(END,"Enter name")
# input_.grid(row=2,column=1)

text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(END,"This if for Multiline commands!!")
text.grid(column=1,row=5)

screen.mainloop()