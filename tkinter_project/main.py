from tkinter import *
from tkinter import END

screen = Tk()
screen.title("Miles To Km Converter")
screen.minsize(width=300,height=150)
# screen.config(padx=20,pady=20)

label=Label(text="miles" , font=("consoles",12)).place(x=210,y=20)
# label.grid(row=1,column=3)
# label.config(padx=100,pady=20)
label2=Label(text="is equal to",font=("consoles",12)).place(x=60,y=60)
label3=Label(text="Km",font=("consoles",12))
label3.place(x=210,y=60)
label3.config(padx=10,pady=0)
label4 =Label(text="0",font=("times new roman",14))
label4.place(x=150,y=60)

def button_click():
    calculate = round(float(miles.get())*1.609,1)
    label4.config(text=f"{calculate}")

miles=Entry(width=7,font=("times new roman",12))
miles.place(x=150,y=20)
# input.grid(row=1,column=2)



# input2=tkinter.Label(text="",font=("times new roman",14)).place(x=150,y=40)


button=Button(text="Calculate",command=button_click,font=("consolas",10)).place(x=150,y=100)

screen.mainloop()