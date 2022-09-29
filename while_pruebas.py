print("ingrese un numero")
num=int(input())
l = num-1
while num >= 0:
    print(num)
    while l > 1:
        print(l)
        l = l - 1
    num = num - 1

i = 1
while i > 0:
    print(i)
    i = i+ 1
print("Terminé")

promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "
grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: " + str(promedio))