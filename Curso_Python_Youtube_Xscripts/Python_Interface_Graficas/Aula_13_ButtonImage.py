#  --*--     coding:utf-8 --*-- 
from tkinter import *

master = Tk()
master.minsize(300,100)
master.geometry("320x100")


diretorioImagens =r"F:\VersionCode\AprendendoPython\AprendendoPython\Curso_Python_DSA\Cap05\Jogo_Forca\Imagens"

photo=PhotoImage(file=diretorioImagens +"\letraA.PNG")
photo.height=30
photo.width=200
b = Button(master,image=photo, text="OK",  height=50, width=200, compound=LEFT)
b.pack()

mainloop()