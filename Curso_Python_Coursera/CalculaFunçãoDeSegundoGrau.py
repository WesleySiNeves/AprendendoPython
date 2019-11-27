
import math

A =  float(input("digite o valor de A:"))
B =  float(input("digite o valor de B:"))
C =  float(input("digite o valor de C:"))


#---------------------------------------------------------
# Regra: f(x) = ax2 + bx + c
# 
# Qualquer pessoa pode usar e modificar esse programa.
#---------------------------------------------------------
#x= (A * (x ** 2))  + (B * x)  + C

Delta =(B ** 2) -4 * A * C


if(Delta == 0):
        ValorX1 = (-(B) + math.sqrt(Delta)) / (2 * A)
        print("Só existe uma raiz é:",ValorX1)
else:
        if(Delta < 0):
            print("Essa equação não possue valores reais:")
        else:
            ValorX1 = (-(B) + math.sqrt(Delta)) / (2 * A)
            ValorX2 = (-(B) - math.sqrt(Delta)) / (2 * A)
            print("A primeira raiz X1 é:",ValorX1)
            print("A segunda  raiz X2 é:",ValorX2)










