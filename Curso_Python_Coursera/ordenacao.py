def main():
    '''
    Esse é um docstring, usado para explicar o que o
    programa faz.
    '''
    # coloque os comandos de seu programa abaixo
    Numero1 = int(input("Digite um número:"))
    Numero2 = int(input("Digite outro um número:"))
    Numero3 = int(input("Digite outro um número:"))

    if((Numero1 < Numero2) and (Numero2 <  Numero3) ):
        print("crescente")
    else:
        print("não está em ordem crescente")
    

    # FIM DO PROGRAMA

#-----------------------------------------------------
# Mantenha e não modifique o código abaixo
#-----------------------------------------------------
if __name__ == '__main__':
    main() # chamada que inicia o programa
