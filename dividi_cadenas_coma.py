lista = "avión, coche, motocicleta, barco, submarino"
palabras = lista.split()

for palabra in palabras:
    print (palabra.strip())

palabras = lista.split(",")
for palabra in palabras:
    print (palabra.strip())