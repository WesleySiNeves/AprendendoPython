from functools import *
from tkinter import *

main_window = Tk()

def btnOk_click(botao):
    print(txt_valor.get())
    lblvalor["text"] = txt_valor.get()

txt_valor = Entry(main_window,width=40)
txt_valor.place(x=10,y=30)

btnOk = Button(main_window,width=40,text="Ok")
btnOk["command"] =partial(btnOk_click,btnOk)
btnOk.place(x=10,y=50)

lblvalor = Label(main_window,width=40,text="Ola")
lblvalor.place(x=10,y=100)






main_window.geometry("400x400+100+100")
main_window.mainloop()

