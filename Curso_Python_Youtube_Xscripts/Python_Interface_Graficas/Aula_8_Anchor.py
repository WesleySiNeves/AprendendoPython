from functools import *
from tkinter import *

main_window = Tk()

lbl1 = Label(main_window,text="TOP",bg="red")
lbl2 = Label(main_window,text="LEFT",bg="blue")
lbl3 = Label(main_window,text="BOTTOM",bg="green")
lbl4 = Label(main_window,text="RIGHT",bg="green")

lbl1.pack(side=TOP,fill=X)
lbl2.pack(side=RIGHT)
lbl3.pack(anchor=NW)
lbl4.pack(anchor=SW)


main_window.geometry("400x400+100+100")
main_window.mainloop()
