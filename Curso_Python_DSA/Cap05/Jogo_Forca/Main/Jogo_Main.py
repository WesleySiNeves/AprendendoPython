import tkinter
from AprendendoPython.Curso_Python_DSA.Cap05.Jogo_Forca.Classes import Jogo


main_window = tkinter.Tk()  #  Tk() e a classe principal
main_window["bg"] ="green"
main_window.minsize(300,100)
main_window.title("Jogo Forca")

jogo = Jogo(main_window)










main_window.geometry("800x600+100+100")

## Executa o programa ,mostrando a janela
main_window.mainloop()

