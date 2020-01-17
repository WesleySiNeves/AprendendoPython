
def fatorial(n):
    if(n ==1):
        return 1
    
    return fatorial(n-1) * n

print(fatorial(6))