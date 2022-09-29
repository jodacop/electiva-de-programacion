# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:15:50 2022

@author: Jonathan Coronado
"""
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