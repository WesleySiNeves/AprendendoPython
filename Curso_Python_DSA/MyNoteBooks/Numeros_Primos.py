
limite = 30
numeros_Primos = []
is_primo = False
quantidade_divisores = 0

for numero in range(1,limite,1):
    is_primo = False
    if(numero ==1):
        is_primo = True
        numeros_Primos.append(numero)
        continue

    teste =1
    quantidade_divisores =0
    while(teste <= numero):
        if(numero % teste ==0):
            quantidade_divisores +=1
        
        teste +=1;
        
        if(quantidade_divisores > 2):
            break
    
    if(quantidade_divisores==2):
        numeros_Primos.append(numero)
        
print(numeros_Primos)

for i in numeros_Primos:
     print(str(i) + " é um número primo")
        
        
        
        
