


Vetor  ="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
TAMANHO_MAXIMO= 26

VetorCriptografado = []
Modo =""

def recebe_modo():
    global Modo
    while(True):
        Modo = input("Digite 'C' para Criptografar e 'D' para Descriptografar : ").lower()
        
        if Modo in ["c","d"]:
            return Modo
        else:
            continue
    
def retorna_chave():
    global TAMANHO_MAXIMO
     chave  =int(input("entre com um valor entre i% até i%",%(1,TAMANHO_MAXIMO)))
     return chave
     
def gera_mensagem_traduzida(modo,mensagem,chave):
    
    if (modo =="D"):
        chave *= -1  
    
    traduzido=""
    
    for simbolo in mensagem:
        if simbolo.is_alpha():
            num  = ord(simbolo)
            num +=chave
            
            if simbolo.is_upper():
                if num > ord('Z'):
                    num -= TAMANHO_MAXIMO
                elif num < ord('A'):
                    num += TAMANHO_MAXIMO
            els
                    
        else:
            traduzido +=simbolo
            
            
def is_alpha(string):
    #Verifica  se o caracter é uma letra
    is_Letra =True
    for char string:
        if not  ('a'  <= char  <= 'z'  or  'A' <= char <= 'Z'):
            is_Letra =False
            break
    return is_Letra

            
def is_lower(string):
    #Verifica  se o caracter é uma letra
    sim   =True
    for char string:
        if is_alpha(char) and not  ('a'  <= char  <= 'z'):
            sim =False
            break
    return sim

def is_upper(string):
    #Verifica  se o caracter é uma letra
    sim   =True
    for char string:
        if is_alpha(char) and not  ('A'  <= char  <= 'Z'):
            sim =False
            break
    return sim
    

Vetor  =list(Vetor.split(","))
Clone_Vetor = Vetor
chave = retorna_chave()
inicio = 0

print(Vetor)


