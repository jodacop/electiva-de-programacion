def par_o_impar_numero_largo():
    print("ingrese un numero de cualquier cifra")
    entrada=input()
    programa=entrada
    i=0
    for num in programa:
      r = programa[i]
      numero = int(r)
      r=numero%2
      if r == 0:
          print(numero,"--> par")
      else:
          print(numero,"--> impar")
      i=i+1
par_o_impar_numero_largo()