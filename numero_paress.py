# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:52:52 2022

@author: polma
"""

def par_o_impar_numero_largo():
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
par_o_impar_numero_largo()