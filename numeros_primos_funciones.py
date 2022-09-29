# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:23:51 2022

@author: Jonathan Coronado
"""
def primo():
    print("el numero es primo")
def noprimo():
    print("el numero no es primo")
def condicion(num,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,dies):
    if num >= 0:
        if num > 10:
            if dos == 0 or tres == 0 or cuatro == 0 or cinco == 0 or seis == 0 or siete == 0 or ocho == 0 or nueve == 0 or dies == 0:
                noprimo()
            else:
                primo()
        else:
            if num == 2 or num == 3 or num == 5 or num == 7:
                primo()
            else:
                noprimo()
    else:
        print("valor no valido")
    
def main():
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
    condicion(num,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,dies)
main()