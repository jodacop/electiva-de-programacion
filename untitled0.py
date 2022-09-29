# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:35:06 2022

@author: polma
"""

import os
def ingreso(num):
    num = input()
    return num
def parinpar(num):
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
     if prom >= 3 and prom <= 5:
         print("aprobo")
     elif prom < 3 and prom >= 0:
         print("reprobo")
     else:
         print("valor no valido")
    except:
         print("ERROR------Ingrese solo numeros -_-")
num = 0    

def init():
 print('')
 print('--------- MENU ---------')
 print('--------- Seleccione el programa ---------')
 print('1. par inpar')
 print('2. Cuadratica')
 print('3. Salir del programa')
 print('----------------------------------------------------------')
 print('')
 return int(input("Ingrese la opción del menu a la que desea acceder: "))

def menu():
 option = init()
 if option == 1:
  #os.system ("clear") # unix
  os.system ("cls") # Windows
  parinpar(num)
  menu()
 elif option == 2:
  os.system ("cls") # Windows
  menu()
 elif option == 3:
  os.system ("cls") # Windows
  print("Opción 3")
  quit()
 else:
  print("--------- Gracias por utilizar la aplicación ---------")
  quit()
  
menu()