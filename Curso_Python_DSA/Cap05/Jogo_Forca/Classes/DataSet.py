import random
import json

class DataSet():
     def __init__(self,ListaPerguntas = [],DiretorioArquivos =""):
         self.Perguntas = ListaPerguntas
         self.DiretorioArquivos =DiretorioArquivos
         self.NomeArquivoPerguntas = "perguntas.json"

     def __len__(self):
         return  len(self.Perguntas)


     def InitDataSet(self):
         
         if(len(self.DiretorioArquivos) ==0):
             self.DiretorioArquivos =r"F:/VersionCode/AprendendoPython/AprendendoPython/Curso_Python_DSA/Cap05/Jogo_Forca/Arquivos/"
        
        arquivo = open(self.DiretorioArquivos + self.NomeArquivoPerguntas,'r')
        texto = arquivo.read()
        data = json.loads(texto)
         
        
