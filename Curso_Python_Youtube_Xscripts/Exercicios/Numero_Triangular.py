numero = int(input("Digite um numero:"))

primeiro  =1
segundo =2
terceiro =3
triangular=False

while (primeiro <=numero):
    valor = (primeiro * (segundo) * (terceiro))
    
    if (valor ==numero):
        triangular =True
        break
     
    primeiro +=1
    segundo +=1
    terceiro +=1

if(triangular):
    print("Numero Triangular")
else:
    print("Numero não é Triangular")
    