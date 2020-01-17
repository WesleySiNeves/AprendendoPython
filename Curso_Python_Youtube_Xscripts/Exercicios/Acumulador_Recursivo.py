
def acumulador(n):
    if(n ==1):
        return 1
    
    return acumulador(n-1) + n

print(acumulador(6))


print(1+2+3+4+5+6)