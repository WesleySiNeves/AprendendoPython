from functools import *
from tkinter import *

main_window = Tk()

#Definição de Funcoes

def btn_Click(btn):
    btn["text"] ="Hahah"


## Forma em python de passar paramentro para a função como um "delegate"
btn_1 =Button(main_window,text="btn_1",width=30)
btn_1["command"] =partial(btn_Click,btn_1)
btn_1.place(x=60,y=100)

btn_2 =Button(main_window,text="btn_2",width=30)
btn_2["command"] =partial(btn_Click,btn_2)
btn_2.place(x=60,y=130)



    





##Enviar para o metodo geometry uma string no seguinte estrutura
#LxA+E+T
#L = largura
#x caracter fixo
#A Altura
#E quantidade pixel de distancia da esquerda
#T quantidade pixel de distancia do topo
#exemplo : 300x300+100+100
main_window.geometry("300x300+100+100")
main_window.mainloop()