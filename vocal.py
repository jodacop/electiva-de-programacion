# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:01:52 2022

@author: Jonathan
"""

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