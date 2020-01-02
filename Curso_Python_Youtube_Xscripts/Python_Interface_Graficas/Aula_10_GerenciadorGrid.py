from functools import *
from tkinter import *

main_window = Tk()

lbl1 = Label(main_window,text="TOP",bg="red")
lbl2 = Label(main_window,text="LEFT",bg="blue")
lbl3 = Label(main_window,text="BOTTOM",bg="green")
lbl4 = Label(main_window,text="RIGHT",bg="black")



lbl1.grid(row=1)
lbl2.grid(row=2,column=1)
lbl3.grid(row=3,column=2)
lbl4.grid(row=4,column=3)


main_window.geometry("400x400+100+100")
main_window.mainloop()
