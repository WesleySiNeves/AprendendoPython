

arquivo = open("meuarquivo.txt",'r')

print(arquivo.read())


arquivo.close()


# w => write
# 'r' => read
# 'a' => append

#segundo Exemplo


arquivo = open("meuarquivo.txt",'r')

print(arquivo.readlines())



#arquivo.close()