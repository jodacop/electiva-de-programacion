def factorial():
    print("Ingrese el numero para obtener el factorial")
    numero = int(input())
    numer = numero
    factorial = 1
    for factorial in range (1,numero):
        numer = numer - 1
        numero = numero * (numer)
        factorial = factorial + 1
    print("el resultado es: ",numero)
factorial()