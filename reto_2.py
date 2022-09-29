def analiza_cadena(caden):
  cuenta_letra=cantidad=0
  for letra in cadena:
    if letra == " ":
      if cuenta_letra>5:
        cantidad=cantidad+1
        b = cadena[cuenta_letra]
        b = "f"
        cadena[cuenta_letra] = b
      cuenta_letra=0
    else:
      cuenta_letra=cuenta_letra+1
  if cuenta_letra>5:
    cantidad = cantidad+1
  print("----")
  print(cadena)
  print("---")
  print(cantidad," palabras trienen mas de 5 letras")

cadena=input()
print("cadena a analizar -->",cadena)
analiza_cadena(cadena)