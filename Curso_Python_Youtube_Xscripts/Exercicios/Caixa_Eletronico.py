
valor_saque =  int(input("Qual é o valor do Saque ?"))

# if(valor_saque <10 or valor_saque >600):
#     print("Valor do saque invalido! digite um valor entre 10 e 600.")


notas = [100,50,20,10,5,2]

saida =""


resto =1
iterador = 0
while resto != 0:
    nota = notas[iterador]
    quantidade_notas = valor_saque // nota
    resto =valor_saque % nota
    iterador +=1

    if(quantidade_notas >= 1):
        saida +="{0} nota(s) de {1} \n".format(quantidade_notas,nota)
        valor_saque = (valor_saque - (quantidade_notas * nota))

print(saida)