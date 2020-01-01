from tkinter import *

main_window = Tk()  #  Tk() e a classe principal


#Definição de Funções
def  btnOk_Click():
    texto =lblteste["text"]
    
    if(texto =="Funcionou"):
        lblteste["text"] ="Teste"
    else:
        lblteste["text"] ="Funcionou"

#Criação de componentes
btnOk = Button(main_window,text="OK",width =20,command=btnOk_Click)
btnOk.place(x=100,y=100)

lblteste =Label(main_window,text="teste",width =30)
lblteste.place(x=120,y=120)








main_window.title("Alguma coisa")
main_window["bg"] ="green"
#Enviar para o metodo geometry uma string no seguinte estrutura
#LxA+E+T
#L = largura
#x caracter fixo
#A Altura
#E quantidade pixel de distancia da esquerda
#T quantidade pixel de distancia do topo
#exemplo : 300x300+100+100
main_window.geometry("800x300+100+100")

## Executa o programa ,mostrando a janela
main_window.mainloop()

