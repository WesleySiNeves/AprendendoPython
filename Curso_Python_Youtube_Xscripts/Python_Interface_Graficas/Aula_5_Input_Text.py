from functools import *
from tkinter import *


main_window  = Tk()

txt = Entry(width=80)
txt.place(x=100,y=100)

btn = Button(main_window,width=30)
btn.place(x=100,y=100)


main_window.geometry("400x400+300+300")
main_window.mainloop()