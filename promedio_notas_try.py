# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:44:09 2022

@author: Jonathan Coronado
"""
def ingreso(num):
    num = input()
    return num
def main(num):
    try:
     i = 0
     sal = 0
     while i <= 2:
        print("Ingrese la nota ", i + 1)
        num = ingreso(num)
        num = float(num)
        sal = sal + num
        i = i + 1
     prom = sal / i
     print("el promedio de notas es: ", prom)
    except:
         print("ERROR------Ingrese solo numeros -_-")
num = 0    
main(num)
