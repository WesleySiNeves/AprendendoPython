from functools import *
from tkinter import *

main_window = Tk()


#Funções

def btnLogin_click():
    user = str(txtUser.get())
    password  =str(txtSenha.get())
    
    if(len(user) == 0 or len(password) ==0):
        lblValidacao["text"] ="O campo User e senha são obrigatorios!"
    

lblUser = Label(main_window,text="Usuário")
lblSenha = Label(main_window,text="Senha")
txtUser = Entry(main_window,width=30)
txtSenha = Entry(main_window,width=30)
btnLogin = Button(main_window,text="Entrar")
btnLogin["command"] =partial(btnLogin_click)
lblValidacao = Label(main_window,text="*")


lblUser.grid(row=1,column=1)
txtUser.grid(row=1,column=2)
lblSenha.grid(row=2,column=1)
txtSenha.grid(row=2,column=2)
btnLogin.grid(row=3,column=2)



main_window.geometry("300x300+100+100")
main_window.mainloop()
