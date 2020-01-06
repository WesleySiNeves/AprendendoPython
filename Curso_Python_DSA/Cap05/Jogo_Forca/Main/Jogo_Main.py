import tkinter

import random
from tkinter import *
import json
from functools import *
from PIL import Image, ImageTk




class Perguntas():
    def __init__(self, numero=0, pergunta="", dica="", resposta=""):
        self.numero = numero
        self.pergunta = pergunta
        self.dica = dica
        self.resposta = resposta



class Jogo():
    def __init__(self, main_window, diretorio=""):
        self.main_window = main_window
        self.DiretorioArquivos = self.initdiretorioArquivos()
        self.NomeArquivoPerguntas = self.initdiretorioArquivoPerguntas()
        self.diretorioimagens = diretorio
        self.letrasdoalfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                 "R", "S", "T", "U", "V", "X", "Z"]
        self.listaImagensErro =[]
        self.pergunta_vez =()
        self.perguntas_efeituadas =[]
        self.QuantidadeErros =0
        self.letras_escolhidas =[]
        self.data_source_perguntas =self.initDataSource()
        self.IniciarLayout()

    def initdiretorioArquivoPerguntas(self):
        return "perguntas.json"
    
    def initdiretorioArquivos(self):
        return r"F:/VersionCode/AprendendoPython/AprendendoPython/Curso_Python_DSA/Cap05/Jogo_Forca/Arquivos/"
    
   # inicia todo o layout do jogo #
    def IniciarLayout(self):
        self.diretorioimagens = self.getDiretorioImagens()
        self.iniciar_Boneco()
        self.iniciar_pergunta()
        self.iniciar_componentes()
        self.iniciar_Botoes_Letras_Alfabeto()

    def initDataSource(self):
        arquivo = open(self.DiretorioArquivos + self.NomeArquivoPerguntas, 'r')
        texto = arquivo.read()
        data = json.loads(texto)
        retorno = []

        for item in (data):
            pergunta = Perguntas()
            pergunta.numero = item["numero"]
            pergunta.pergunta = item["pergunta"]
            pergunta.dica = item["dica"]
            pergunta.resposta = item["resposta"]
            retorno.append(pergunta)

        return list(retorno)


    def getDiretorioImagens(self):
        configurationFile = "get configuration file"

        if (1 == 1):
            return r"F:\VersionCode\AprendendoPython\AprendendoPython\Curso_Python_DSA\Cap05\Jogo_Forca\Imagens"
   
    def  iniciar_Boneco(self):
        
        diretorio  = self.getDiretorioImagens()

        imagem_erro_zero = Image.open( diretorio + "\erroZero.PNG")
        photo_zero = ImageTk.PhotoImage(imagem_erro_zero)

        imagem_erro_um = Image.open(diretorio + "\erroUm.PNG")
        photo_um = ImageTk.PhotoImage(imagem_erro_um)

        imagem_erro_dois = Image.open(diretorio + "\erroDois.PNG")
        photo_dois = ImageTk.PhotoImage(imagem_erro_dois)

        imagem_erro_tres = Image.open(diretorio + "\erroTres.PNG")
        photo_tres = ImageTk.PhotoImage(imagem_erro_tres)
        
        imagem_erro_quatro = Image.open(diretorio + "\erroQuatro.PNG")
        photo_quatro = ImageTk.PhotoImage(imagem_erro_quatro)
        
        imagem_erro_cinco = Image.open(diretorio + "\erroCinco.PNG")
        photo_cinco = ImageTk.PhotoImage(imagem_erro_cinco)
        
        imagem_erro_seis = Image.open(diretorio + "\erroSeis.PNG")
        photo_seis = ImageTk.PhotoImage(imagem_erro_seis)

        erro_zero = (0,photo_zero)
        erro_um = (1, photo_um)
        erro_dois = (2, photo_dois)
        erro_tres = (3, photo_tres)
        erro_quatro = (4, photo_quatro)
        erro_cinco = (5, photo_cinco)
        erro_seis = (6, photo_seis)
        self.listaImagensErro.append(erro_zero)
        self.listaImagensErro.append(erro_um)
        self.listaImagensErro.append(erro_dois)
        self.listaImagensErro.append(erro_tres)
        self.listaImagensErro.append(erro_quatro)
        self.listaImagensErro.append(erro_cinco)
        self.listaImagensErro.append(erro_seis)


        labelBoneco = Label(image=photo_zero)
        labelBoneco.image = photo_zero  # this line need to prevent gc
        labelBoneco.grid(row=0,column=0)
        
    def escolher_pergunta(self):
        data = self.data_source_perguntas
        escolha = random.randint(0, len(data) - 1)
        perguntaEscolhida =data[escolha]
        
        self.pergunta_vez = perguntaEscolhida
        self.perguntas_efeituadas.append(perguntaEscolhida)
        
        return perguntaEscolhida
  
    def iniciar_pergunta(self):
            
        perguntaEscolhida   =self.escolher_pergunta()
        
        lblPergunta = Label(self.main_window,text = perguntaEscolhida.pergunta, height =2 ,width =20)
        lblPergunta.config(font=("Courier", 12))
        lblPergunta.grid(row=0,column=1)
        
        lblDica = Label(self.main_window,text = "Dica:"+perguntaEscolhida.dica, height =2 ,width =20)
        lblDica.config(font=("Courier", 12))
        lblDica.grid(row=0,column=2)
       
    def iniciar_componentes(self):
        lblLetrasEscolhidas = Label(self.main_window,text = self.letras_escolhidas, height =2 ,width =20)
        lblLetrasEscolhidas.config(font=("Courier", 12))
        lblLetrasEscolhidas.grid(row=3,column=1)
    
    def iniciar_Botoes_Letras_Alfabeto(self):
        
        incrementColumn = 0
        for letra in list(self.letrasdoalfabeto):
            botao = Button(self.main_window, text=letra, height=5, width=5, bg="red")
            botao["command"] = partial(self.btn_click, botao)
            botao.grid(row=3,column=incrementColumn)
            incrementColumn += 1
  
    def hasLetraNaResposta(self, pergunta, letraRespondida):
        resposta = pergunta.resposta

        if (str(pergunta.resposta).find(letraRespondida) == -1):
            return False;
        else:
            return True;

    def getQuantidadeLetras(self):
        perg = self.iniciar_pergunta()
        return len(perg.resposta)

    def btn_click(self, botao):
      
      letra = botao["text"]
      
    #   if(self.letras_escolhidas.count(letra) > 0):
          
          
      
      if(self.hasLetraNaResposta(self.pergunta_vez,letra)):
          self.PreencherLetra(letra)
      else:
          self.incrementarErros()
          
      if(self.QuantidadeErros==7):
           self.GameOver()
          
    def PreencherLetra(self):
        pass
         
    def incrementarErros(self):
        self.QuantidadeErros +=1
        self.IncrementarImagenBonecoErro()

    def GameOver(self):
        pass

    def IncrementarImagenBonecoErro(self):
        
        foto = self.listaImagensErro[self.QuantidadeErros]
        labelBoneco = Label(image=foto[1])
        labelBoneco.image = foto[1]  # this line need to prevent gc
        labelBoneco.grid(row=0,column=0)

        # label = Label(image=photo_zero)
        # label.image = photo_zero  # this line need to prevent gc
        # label.grid(row=0,column=0)
   
    
# root = tkinter.Tk()
# Application(root)
# root.mainloop()    
    

main_window = tkinter.Tk()  #  Tk() e a classe principal
main_window["bg"] ="green"
main_window.title("Jogo Forca")
jogo = Jogo(main_window)
main_window.geometry("800x600+300+300")
main_window.mainloop()    
    
# ## Executa o programa ,mostrando a janela


