# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f6eaEqiwAk9p1knga_EY5tHzKmyEPbAi
"""

def suma(a,b):
  return a + b
  
print("Ingrese el primer numero:")
a = int(input())
print("Ingrese el segundo numero:")
b = int(input())
print("El resultado es: ", suma(a,b))
c=suma(a,b)
while c <= 10:
  print("Ingrese el primer numero:")
  a = int(input())
  print("Ingrese el segundo numero:")
  b = int(input())
  print("El resultado es: ", suma(a,b))
  c=suma(a,b)
  d=suma(a,b)
  f = d
  while d > 10:
    d = 1
  while f <= 10:
    print("quiere sumar de nuevo?   1->si, 2->no")
    e = int(input())
    while e == 1:
      c = 1
      f = 11
      e = 3
    while e == 2:
      c = 11
      f = 11
      e = 1
    #######

def cuadraticapos(a,b,c):
  raisdenp = ((b**2) - (4 * a * c))**0.5
  resultadop = (b + raisdenp) / (2 * a)
  return resultadop

def cuadraticaneg(a,b,c):
  raisdenp = ((b**2) - (4 * a * c))**0.5
  resultadop = (b - raisdenp) / (2 * a)
  return resultadop

print("--tomando en cuenta la ecuacion cuadratica--")
print("-- a(x^2) + b(x) + c = 0 --")

print("-- ingrese los valores de: a --")
a = float(input())

print("-- ingrese los valores de: b --")
b = float(input())

print("-- ingrese los valores de: c --")
c = float(input())

print("el resultado 1 es: x=", cuadraticapos(a,b,c))
print("el resultado 2 es: x=", cuadraticaneg(a,b,c))

print("desea cambiar algun valor? si->1, no->cualquier otro numero")
cambiar = int(input())

while cambiar == 1:
    print("que valor desea cambiar? a->1, b->2, c->3")
    vcambio = int(input())
    if vcambio == 1:
        print("ingrese el nuevo valor de a")
        a = float(input())
        print("el resultado 1 es: x=", cuadraticapos(a,b,c))
        print("el resultado 2 es: x=", cuadraticaneg(a,b,c))
    
    elif vcambio == 2:
        print("ingrese el nuevo valor de b")
        b = float(input())
        print("el resultado 1 es: x=", cuadraticapos(a,b,c))
        print("el resultado 2 es: x=", cuadraticaneg(a,b,c))
    
    elif vcambio == 3:
        print("ingrese el nuevo valor de c")
        c = float(input())
        print("el resultado 1 es: x=", cuadraticapos(a,b,c))
        print("el resultado 2 es: x=", cuadraticaneg(a,b,c))

    else:
        print("gracias")
    
    print("desea cambiar algun valor? si->1, no->cualquier otro numero")
    cambiar = int(input())
    #####

def suma(a,b):
  return a + b

def ciclo():
 c = 1
 while c <= 10:
  a = 0
  b = 0
  print("Ingrese el primer numero:")
  a = int(input())
  print("Ingrese el segundo numero:")
  b = int(input())
  print("El resultado es: ", suma(a,b))
  c=suma(a,b)
  d=suma(a,b)
  f = d
  while d > 10:
    c=11
    d = 1
  while f <= 10:
    print("quiere sumar de nuevo?   1->si, 2->no")
    e = int(input())
    while e == 1:
      c = 1
      f = 11
      d = 11
      e = 3
    while e == 2:
      c = 11
      f = 11
      e = 1 
ciclo()
########

a=b=c=800
print(a)
print(b)
print(c)
########

list(range(2,18))
######

def rango():
  print(list(range(2,18)))
rango()
########

def rango():
  a = list(range(5,35,2))
  print(type(a))
  for i in a:
    print(i*i)
rango()
#####

def rango():
  a = list(range(5,35,2))
  print(type(a))
  for i in range(15):
    print(a[i]**2)
rango()
#####

def rango():
  a = list(range(5,35,2))
  print(type(a))
  i=0
  while i <= 14:
    print(a[i]**2)
    i+=1
rango()
######



def vocal(val):
    if val == "a" or val == "e" or val == "i" or val == "o" or val == "u":
        return True
    else:
        return False
def main():
    print("ingrese una caracter")
    val = input()
    valor = vocal(val)
    print(valor)
main()
######

def main():
    print("ingrese un numero:")
    num = int(input())
    num = num % 2
    if num == 0:
        print("el numero es par")
    else:
        print("el numero es inpar")
main()
######

#es numero enteros+
pin = input()

print(pin.isnumeric())
#####

#es letra true, solo para una letra u una palabra, con espacio no funciona

pin = input()

print(pin.isalpha())
############

#es decimal
pin = input()

print(pin.isdecimal())
########

# es minusculula 
s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  #########

# numero par
def main(num):
    try: 
      num = int(num) % 2
      if num == 0:
        print("el numero es par")
      else:
        print("el numero es inpar")
    except:
        print(" ERROR---ingrese solo numeros")
     
print("ingrese numeros")
num = input()

main(num)
##########

def numero(val):
    valo = val.isdecimal()
    if valo == True:
        return True
    else:
        return False

def letra(val):
    vali = val.isalpha()
    if vali == True:
        return True
    else:
        return False
def main():
    print("ingrese un caracter o un numero")
    val = input()
    valor = numero(val)
    let = letra(val)
    if valor == True:
        print("el dato es un numero")
    elif let == True:
        print("el dato es una letra")
        
main()
##########

#promedio notas
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
parinpar(num)
#######

#identifa par y no par
print("ingrese un numero de 4 digitos")
num = int(input())
div = num / 1000
res = num % 1000
rest = res * 0.001
div = div - rest
divi = div % 2
if divi == 0:
    print("el numero ", div, " es par")
else:
    print("el numero ", div, " es inpar")
seg = res / 100
resis = res % 100
muls = resis * 0.01
restad = seg - muls
vals = restad % 2
if vals == 0:
    print("el numero ", restad, " es par")
else:
    print("el numero ", restad, " es inpar")
ter = resis / 10
resit = resis % 10
mult = resit * 0.1
restat = ter - mult
valt = restat % 2
if valt == 0:
    print("el numero ", restat, " es par")
else:
    print("el numero ", restat, " es inpar")
cuar = resit / 1
resic = resit % 1
mulc = resic * 1
restac = cuar - mulc
valc = restac % 2
if valc == 0:
    print("el numero ", restac, " es par")
else:
    print("el numero ", restac, " es inpar")
#############

#par e impar con funciones
def mil(num,res):
    div = num / 1000
    res = num % 1000
    rest = res * 0.001
    div = div - rest
    divi = div % 2
    return divi
def cien(res, resis):
    seg = res / 100
    resis = res % 100
    muls = resis * 0.01
    restad = seg - muls
    vals = restad % 2
    return vals
def dies(resis, resit):
    ter = resis / 10
    resit = resis % 10
    mult = resit * 0.1
    restat = ter - mult
    valt = restat % 2
    if valt == 0:
        print("el numero ", restat, " es par")
    else:
        print("el numero ", restat, " es inpar")
def once(resit):
    cuar = resit / 1
    resic = resit % 1
    mulc = resic * 1
    restac = cuar - mulc
    valc = restac % 2
    if valc == 0:
        print("el numero ", restac, " es par")
    else:
        print("el numero ", restac, " es inpar")
def ingreso(num):
    num = input()
    return num
def main(num,res,resis):
    num = ingreso(num)
    num = int(num)
    divi = mil(num,res)
    if divi == 0:
        print("el numero es par")
    else:
        print("el numero es inpar")
    vals = cien(res, resis)
    if vals == 0:
        print("el numero es par")
    else:
        print("el numero es inpar")
print("ingrese un numero de 4 digitos")
res = 0
resis = 0
num = 0
main(num,res,resis)
#######

import os

def init():
 print('')
 print('--------- MENU ---------')
 print('--------- Seleccione el programa ---------')
 print('1. suma con solo while')
 print('2. Cuadratica')
 print("3. Rango")
 print("4. Eleccion de vocal")
 print("5. Es vocal?")
 print("6. Numero par e impar")
 print("7. Numero par con try")
 print("8. Diferentes usos del is----")
 print("9 Promedio de notas")
 print("10. definir si los numero son pares")
 print("11. factorial")
 print('3. Salir del programa')
 print('----------------------------------------------------------')
 print('')
 return int(input("Ingrese la opci??n del menu a la que desea acceder: "))

def menu():
 option = init()
 if option == 1:
  #os.system ("clear") # unix
  os.system ("cls") # Windows
  menu()
 elif option == 2:
  os.system ("cls") # Windows
  menu()
 elif option == 3:
  os.system ("cls") # Windows
  print("Opci??n 3")
  quit()
 else:
  print("--------- Gracias por utilizar la aplicaci??n ---------")
  quit()
  
menu()
#########

import os

def init():
  print('')
  print('--------- MENU ---------')
  print('--------- Seleccione el programa ---------')
  print('1. Ejercicio1')
  print('2. Ejercicio2')
  print('3. Salir del programa')
  print('----------------------------------------------------------')
  print('')
  return int(input("Ingrese la opci??n del menu a la que desea acceder: "))

def menu():
  option = init()
  if option == 1:
    #os.system ("clear") # unix
    os.system ("cls") # Windows
    ejercicio1()
    menu()
  elif option == 2:
    os.system ("cls") # Windows
    ejercicio2()
    menu()
  elif option == 3:
    os.system ("cls") # Windows
    print("Opci??n 3")
    quit()
  else:
    print("--------- Gracias por utilizar la aplicaci??n ---------")
    quit()


menu()
########



num=input("escriba numero de 4 digitos: --->")
print(num)
num=int(num)
print(type(num))
a=num//1000
aa=num%1000
b=aa//100
bb=aa%100
c=bb//10
d=bb%10

print(a,b,c,d)

#############

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
def par_o_impar_numero_largo():
    print("ingrese un numero de 4 cifras")
    entrada=input()
    programa=entrada
    i=0
    while i <= 3: 
      r = programa[i]
      numero = int(r)
      r=numero%2
      if r == 0:
          print(numero,"--> par")
      else:
          print(numero,"--> impar")
      i=i+1
num = 0    

def init():
 print('')
 print('--------- MENU ---------')
 print('--------- Seleccione el programa ---------')
 print('1. promedio notas')
 print('2. numero pares o impares')
 print('3. Salir del programa')
 print('----------------------------------------------------------')
 print('')
 return int(input("Ingrese la opci??n del menu a la que desea acceder: "))

def menu():
 option = init()
 if option == 1:
  #os.system ("clear") # unix
  os.system ("cls") # Windows
  parinpar(num)
  menu()
 elif option == 2:
  os.system ("cls") # Windows
  par_o_impar_numero_largo()
  menu()
 elif option == 3:
  os.system ("cls") # Windows
  print("Opci??n 3")
  quit()
 else:
  print("--------- Gracias por utilizar la aplicaci??n ---------")
  quit()
  
menu()
############

def analiza_cadena(caden):
  #foreach
  for letra in cadena:
    if letra == "a":
      print(letra)
def analiza_cadena_1(caden):
  #foriterador
  long=len(cadena)
  for indice in range(long):
    if cadena[indice] == "a":
      print(cadena[indice])
cadena="20hola!-21?."
print("cadena a analizar -->",cadena)
analiza_cadena(cadena)
analiza_cadena_1(cadena)
######

def analiza_cadena(caden):
  #foreach
  cuenta_letra=cantidad=0
  for letra in cadena:
    print(letra)
    if letra == " ":
      if cuenta_letra>5:
        cantidad=cantidad+1
      cuenta_letra=0
    else:
      cuenta_letra=cuenta_letra+1
  if cuenta_letra>5:
    cantidad = cantidad+1
  print("---")
  print(cantidad," palabras trienen mas de 5 letras")

cadena="holas knjhnjb jffhhj hfffhh"
print("cadena a analizar -->",cadena)
analiza_cadena(cadena)
###########

import os

def analiza_cadena(caden):
  #foreach
  cuenta_letra=cantidad=0
  print(caden)
  for letra in caden:
    if letra == " ":
      if cuenta_letra>5:
        cantidad=cantidad+1
      cuenta_letra=0
    else:
      cuenta_letra=cuenta_letra+1
  if cuenta_letra>5:
    cantidad = cantidad+1
  print("---")
  print(cantidad," palabras trienen mas de 5 letras")

def init():
    print('')
    print('--------- MENU ---------')
    print('--------- Seleccione el programa ---------')
    print('1. contar palabras con mas de 5 letras')
    print('2. Salir del programa')
    print('----------------------------------------------------------')
    print('')
    return int(input("Ingrese la opci??n del menu a la que desea acceder: "))

def menu():
    option = init()
    if option == 1:
        #os.system ("clear") # unix
        os.system ("cls") # Windows
        cadena=input("ingrese las palabras -->")
        print("cadena a analizar -->",cadena)
        analiza_cadena(cadena)
        menu()
    elif option == 2:
        os.system ("cls") # Windows
        print("Opci??n 3")
        quit()
    else:
        print("--------- Gracias por utilizar la aplicaci??n ---------")
        quit()
menu()
###########