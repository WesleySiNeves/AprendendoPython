from functools import *
from tkinter import *

main_window = Tk()

entradas =[]

operandoEsquerda=0
operandoDireita =0
operador =""
result =0

def btnCalcular(botao):
    
    entradas.append(txt_Entrada1.get())
    acao = botao["text"]
    operandoEsquerda = txt_Entrada1.get()
    operandoDireita = txt_Entrada2.get()
    
    if(str(operandoEsquerda).isnumeric() and  str(operandoDireita).isnumeric()):
        operandoEsquerda =int(operandoEsquerda)
        operandoDireita =int(operandoDireita)
             
    if(acao == "+"):
      result = operandoEsquerda  + operandoDireita
            
    
    if(acao == "-"):
        result = operandoEsquerda  - operandoDireita
    
    if(acao == "*"):
        result = operandoEsquerda  * operandoDireita
        
    if(acao == "/"):
        result = operandoEsquerda  / operandoDireita
        
    lblResultado["text"] =str(result)
    

        
    
txt_Entrada1 = Entry(main_window,width=30)
txt_Entrada1.place(x=10,y=30)

txt_Entrada2 = Entry(main_window,width=30)
txt_Entrada2.place(x=10,y=50)


btnSomar = Button(main_window,width=5,text="+")
btnSomar["command"] =partial(btnCalcular,btnSomar)
btnSomar.place(x=10,y=70)



btnSubtrair = Button(main_window,width=5,text="-")
btnSubtrair["command"] =partial(btnCalcular,btnSubtrair)
btnSubtrair.place(x=60,y=70)

btnMultiplicar = Button(main_window,width=5,text="*")
btnMultiplicar["command"] =partial(btnCalcular,btnMultiplicar)
btnMultiplicar.place(x=110,y=70)


btnDividir = Button(main_window,width=5,text="/")
btnDividir["command"] =partial(btnCalcular,btnDividir)
btnDividir.place(x=170,y=70)

lblResultado = Label(main_window,width=40,text="Ola")
lblResultado.place(x=10,y=100)






main_window.geometry("400x400+100+100")
main_window.mainloop()

