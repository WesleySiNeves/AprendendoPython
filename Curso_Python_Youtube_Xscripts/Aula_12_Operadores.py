lista_cores= ["azul","verde","amarelo"]
while True:
    cor = input("Digite uma cor ou '0' para sair:")
    
    if(cor =="0"):
        break;
    
    if(cor in lista_cores):
        print("A cor está dentro dos paramentros!")
    else:
        print("A cor não está dentro dos paramentros!")
    
    
    
    
