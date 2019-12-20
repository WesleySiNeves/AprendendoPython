# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

# dias_descanco = ["sábado","Domingo"]
# dia_semama = input("Que dia é hoje ?")

# if(dia_semama in dias_descanco):
#     print("Dia de descanço")
# else:
#     print("Você precisa trabalhar!")



# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista


# lista_frutas = ["perá","maça","abacate","uva","banana","Morango"]

# if("Morango" in lista_frutas):
#     print("Morango está na lista")
# else:
#     print("Morango não está na lista")


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

# variavel_tupla = (1,2,3,4)
# armazenamento = []

# for  item in variavel_tupla:
#     armazenamento.append(item * 2)
#     print(armazenamento)

# print(armazenamento)


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
# for item in range(100,152,2):
#     print(item)



# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela



# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

# contador =0

# while(contador <=100):
#     contador +=1;
#     if(contador ==23):
#         break;
    
#     print(contador)
    
Par = lambda numero: numero % 2 == 0
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista = []
variavel =4

while variavel==4:
    variavel = input("Digite um numero:");
    variavel = int(variavel)
    if variavel <=20:
        lista.append(variavel);
        variavel = 4;
        print(variavel)
    if(variavel>20):
        variavel =5
        

