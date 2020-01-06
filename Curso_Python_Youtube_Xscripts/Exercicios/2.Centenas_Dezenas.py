
#valor =  input("Digite um numero:")

valor = int(1352)
# if(valor_saque <10 or valor_saque >600):
#     print("Valor do saque invalido! digite um valor entre 10 e 600.")

#Desafio ,Colocar a note de 5
escalas = [(1000,"milhar(res)"),(100,"centena(s)"),(10,"dezena(s)"),(1,"unidade(s)")]

saida =""

escala = escalas[0]


divisaoInteira = 0
for escala in escalas:
    divisaoInteira = valor // escala[0]
    
    if(divisaoInteira > 0):
        resto = valor % escala[0]
        valor = (valor - divisaoInteira * escala[0])
        saida +="{0} {1}\n".format(divisaoInteira,escala[1])


print(saida)




# restante =1
# iterador = 0
# while restante != 0:
#     escala = escalas[iterador]
#     quantidade_escala = valor // escala
#     restante =valor % escala
#     iterador +=1

#     if(quantidade_notas >= 1):
#         saida +="{0} nota(s) de {1} \n".format(quantidade_notas,nota)
#         valor_saque = (valor_saque - (quantidade_notas * nota))

# print(saida)