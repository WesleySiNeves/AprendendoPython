
import random
from tkinter import *
import os
from PIL import Image
import json

DiretorioArquivos =r"F:/VersionCode/AprendendoPython/AprendendoPython/Curso_Python_DSA/Cap05/Jogo_Forca/Arquivos/"
NomeArquivoPerguntas = "perguntas.json"


class Perguntas():
    def  __init__(self,numero = 0,pergunta ="",dica ="",resposta=""):
        self.numero =numero
        self.pergunta =pergunta
        self.dica = dica
        self.resposta = resposta
       

class Jogo():
    def __init__(self,main_window,diretorioImagens ="" ,ListaPerguntas =[],LetrasDoAlfabeto =[]):
        self.ListaPerguntas = ListaPerguntas
        self.main_window =main_window
        self.diretorioImagens =diretorioImagens
        self.LetrasDoAlfabeto = ["A","B","C","D","E","F"]
        self.IniciarLayout()
        
    def IniciarLayout(self):
        if(len(self.diretorioImagens) == 0):
            self.diretorioImagens =r"F:\VersionCode\AprendendoPython\AprendendoPython\Curso_Python_DSA\Cap05\Jogo_Forca\Imagens"

        for letra in  list(self.LetrasDoAlfabeto):
            b = Button(self.main_window,  text=letra, height=50, width=200, compound=LEFT)
            b.pack()
    
    def Jogar(self):
        self.ListaPerguntas =initDataSource();

        erros =0
        perguntas = self.ListaPerguntas
        
        pergunta =  self.getItemASerPerguntado()
        
        while (erros <=7):
            
            letraRespondida = self.getLetraRespondida()
            
            if(self.hasLetraNaResposta(pergunta,letraRespondida)):
                self.PreencherLetra(letraRespondida)
                print("Parabens vc Advinhou")
            else:
                erros +=1
                self.AdcionarImage(erros)
                print("Vc errou")
        
        if (erros ==7):
            self.SetGameOver()
        else:
            self.SetJogadorVenceu()
        
    def hasLetraNaResposta(self,pergunta,letraRespondida):
        resposta = pergunta.resposta
        
        if(str(pergunta.resposta).find(letraRespondida) == -1):
            return False;
        else:
            return True;
        
    
    def getItemASerPerguntado(self):
        data =self.ListaPerguntas
        escolha = random.randint(0,len(data) -1)
        return (data[escolha])
    
    def getQuantidadeLetras(self):
        perg = self.getItemASerPerguntado()
        return len(perg.resposta)
            
                
    def initDataSource(self):
        arquivo = open(DiretorioArquivos + NomeArquivoPerguntas,'r')
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








