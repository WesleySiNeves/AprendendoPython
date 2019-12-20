# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

somar = lambda x,y : x+y
subtrair = lambda x,y : x-y
multiplicar = lambda x,y : x*y
dividir = lambda x,y : x/y



def Calcular(numero1, operacao,numero2):
    valor =0
    if(operacao =="+"):
        valor = somar(numero1,numero2)
    if(operacao =="-"):
        valor = subtrair(numero1,numero2)
    if(operacao =="*"):
        valor = multiplicar(numero1,numero2)
    if(operacao =="/"):
        valor = dividir(numero1,numero2)
    return valor
    
numero1 =  float(input("Digite o primeiro número:"))
operacao = input("operação:")
numero2 =  float(input("Digite o segundo número:"))    

print(Calcular(numero1,operacao,numero2))

# resultado =Calcular(numero1,numero1,numero2);

# print(resultado)
