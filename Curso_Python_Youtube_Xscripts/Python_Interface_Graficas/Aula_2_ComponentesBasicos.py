import tkinter

main_window = tkinter.Tk()  #  Tk() e a classe principal
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

