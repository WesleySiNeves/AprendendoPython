from functools import *
from tkinter import *

main_window = Tk()


#Funções

    

lbl1 = Label(main_window,text="ESPAÇO",width=20,bg="blue",height=3)
lblHorizontal = Label(main_window,text="Horizontal",width=20,bg="red")
lblVertical = Label(main_window,text="Vertical",width=20,bg="red")




lbl1.grid(row=0,column=0)
lblVertical.grid(row=1,column=0)
#lblHorizontal.grid(row=1,column=1)




main_window.geometry("300x300+100+100")
main_window.mainloop()
