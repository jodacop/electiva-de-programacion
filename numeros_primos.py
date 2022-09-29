# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:01:42 2022

@author: Jonathan Coronado
"""
# entrada de datos
print("ingrese un numero")
num = int(input())
dos = num % 2
tres = num % 3
cuatro = num % 4
cinco = num % 5
seis = num % 6
siete = num % 7
ocho = num % 8
nueve = num % 9
dies = num % 10
# condicional
if num >= 0:
    if num > 10:
        if dos == 0 or tres == 0 or cuatro == 0 or cinco == 0 or seis == 0 or siete == 0 or ocho == 0 or nueve == 0 or dies == 0:
            print(" el numero no es primo")
        else:
            print("el numero es primo")
    else:
        if num == 2 or num == 3 or num == 5 or num == 7:
            print("el numero es primo")
        else:
            print("el numero no es primo")
else:
    print("valor no valido")