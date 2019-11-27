quantidadeNumero = int(input("Digite a quantidade Numeros:"))

inicio = 1
NumeroImPar = 1;

while(inicio <=quantidadeNumero):
    if(NumeroImPar % 2 != 0):
        print(NumeroImPar)
        inicio +=1
    NumeroImPar +=1
