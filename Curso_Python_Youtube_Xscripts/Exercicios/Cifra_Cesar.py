
Vetor  ="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"

VetorCriptografado = []
Modo =""
Chave =2

inicio = 0
mover =2


Vetor  =  list(str(Vetor).split(","))
VetorClone = Vetor
tamanho_Maximo = len(VetorClone)

def gerar_vetor_Criptografado():
    global Vetor
    global Chave
    global inicio
    global mover
    
    while inicio <=tamanho_Maximo -1:
            if(inicio <= tamanho_Maximo -1):
                
                if((mover) < tamanho_Maximo -1):
                    VetorCriptografado.append(VetorClone[mover])
                    del VetorClone[mover]
                    mover = mover +1
                else:
                    mover = 0
                
                if(mover <= Chave -1):                    
                    VetorCriptografado.insert(mover,Vetor[mover])
                    
                    
            inicio = inicio +1
                
    print(Vetor);
    print(VetorCriptografado);
        
        
            
        
            
    
        




gerar_vetor_Criptografado()






# Modo = input("Digite 'C' para Criptografar e 'D' para descriptografar:")




