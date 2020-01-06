# import random
# from tkinter import *
# import json
# from functools import *
# from PIL import Image, ImageTk

# DiretorioArquivos = r"F:/VersionCode/AprendendoPython/AprendendoPython/Curso_Python_DSA/Cap05/Jogo_Forca/Arquivos/"
# NomeArquivoPerguntas = "perguntas.json"


# class Perguntas():
#     def __init__(self, numero=0, pergunta="", dica="", resposta=""):
#         self.numero = numero
#         self.pergunta = pergunta
#         self.dica = dica
#         self.resposta = resposta



# class Jogo():
#     def __init__(self, main_window, diretorio="", lista=[]):
#         self.data_source_perguntas = lista
#         self.main_window = main_window
#         self.diretorioimagens = diretorio
#         self.letrasdoalfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
#                                  "R", "S", "T", "U", "V", "X", "Z"]
#         self.listaImagensErro =[]

#         self.IniciarLayout()

#    # inicia todo o layout do jogo #
#     def IniciarLayout(self):
#         self.diretorioimagens = self.getDiretorioImagens()
#         self.iniciarLetrasAlfabeto()
#         self.iniciarImagensBonecos()
#         #pergunta = self.getItemASerPerguntado()
#         #self.perguntas.append(pergunta)



#     def  iniciarImagensBonecos(self):
#         diretorio  = self.getDiretorioImagens()

#         imagem_erro_zero = Image.open( diretorio + "\erroZero.PNG")
#         photo_zero = ImageTk.PhotoImage(imagem_erro_zero)

#         imagem_erro_um = Image.open(diretorio + "\erroUm.PNG")
#         photo_um = ImageTk.PhotoImage(imagem_erro_um)

#         imagem_erro_dois = Image.open(diretorio + "\erroDois.PNG")
#         photo_dois = ImageTk.PhotoImage(imagem_erro_dois)

#         imagem_erro_tres = Image.open(diretorio + "\erroTres.PNG")
#         photo_tres = ImageTk.PhotoImage(imagem_erro_tres)

#         erro_zero = (0,photo_zero)
#         erro_um = (1, photo_um)
#         erro_dois = (2, photo_dois)
#         erro_tres = (3, photo_tres)
#         self.listaImagensErro.append(erro_zero)
#         self.listaImagensErro.append(erro_um)
#         self.listaImagensErro.append(erro_dois)
#         self.listaImagensErro.append(erro_tres)


#         label = Label(image=photo_zero)
#         label.image = photo_zero  # this line need to prevent gc
#         label.grid(row=2, column=1)

#     def iniciarLetrasAlfabeto(self):

#         incrementColumn = 1
#         for letra in list(self.letrasdoalfabeto):
#             botao = Button(self.main_window, text=letra, height=5, width=5, bg="red")
#             botao["command"] = partial(self.btn_click, botao)
#             botao.grid(row=1, column=incrementColumn)
#             incrementColumn += 1

#     def getDiretorioImagens(self):
#         configurationFile = "get configuration file"

#         if (1 == 1):
#             return r"F:\VersionCode\AprendendoPython\AprendendoPython\Curso_Python_DSA\Cap05\Jogo_Forca\Imagens"

#     def hasLetraNaResposta(self, pergunta, letraRespondida):
#         resposta = pergunta.resposta

#         if (str(pergunta.resposta).find(letraRespondida) == -1):
#             return False;
#         else:
#             return True;

#     def getItemASerPerguntado(self):
#         data = self.ListaPerguntas
#         escolha = random.randint(0, len(data) - 1)
#         return (data[escolha])

#     def getQuantidadeLetras(self):
#         perg = self.getItemASerPerguntado()
#         return len(perg.resposta)

#     def initDataSource(self):
#         arquivo = open(DiretorioArquivos + NomeArquivoPerguntas, 'r')
#         texto = arquivo.read()
#         data = json.loads(texto)
#         retorno = []

#         for item in (data):
#             pergunta = Perguntas()
#             pergunta.numero = item["numero"]
#             pergunta.pergunta = item["pergunta"]
#             pergunta.dica = item["dica"]
#             pergunta.resposta = item["resposta"]
#             retorno.append(pergunta)

#         return list(retorno)

#     def btn_click(self, botao):
#         print(botao["text"])
