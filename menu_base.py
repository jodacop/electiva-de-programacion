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
    return int(input("Ingrese la opcion del menu a la que desea acceder: "))

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
        print("Opcion 3")
        quit()
    else:
        print("--------- Gracias por utilizar la aplicacion ---------")
        quit()

menu()