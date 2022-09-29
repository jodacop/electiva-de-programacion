# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:15:50 2022

@author: Jonathan Coronado
"""

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
print(div, rest)