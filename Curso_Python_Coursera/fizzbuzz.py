def main():
    '''
    Esse é um docstring, usado para explicar o que o
    programa faz.
    '''
    # coloque os comandos de seu programa abaixo
    entradaUsuario = int(input("Digite um número:"))

    if((entradaUsuario % 5 == 0 and entradaUsuario % 3 == 0) ):
        print("FizzBuzz")
    else:
        print(entradaUsuario)
    

    # FIM DO PROGRAMA

#-----------------------------------------------------
# Mantenha e não modifique o código abaixo
#-----------------------------------------------------
if __name__ == '__main__':
    main() # chamada que inicia o programa
