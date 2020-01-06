
import  random

numero_lancamento = 100000

dado = [1,2,3,4,5,6]

jogadas = []

for item  in range(0,numero_lancamento):
    jogada = random.choice(dado)
    jogadas.append(jogada)
    numero_lancamento +=1

print(jogadas)

for face in range(1,7):
    calculo =(100 * jogadas.count(face) / numero_lancamento)
    print("A face {0} apareceu {1} vezes que é {2} % ".format(face,jogadas.count(face),calculo))
    


      

    





