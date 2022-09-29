def cuenta_vocales():
    print("ingrese una cadena de caracteres")
    entrada = input()
    a=e=i=o=u=otro=posicion=0
    for analisis in entrada:
        if entrada[posicion] == "a":
            a = a + 1
        elif entrada[posicion] == "e":
            e = e + 1
        elif entrada[posicion] == "i":
            i = i + 1
        elif entrada[posicion] == "o":
            o = o + 1
        elif entrada[posicion] == "u":
            u = u + 1
        elif entrada[posicion] != " ":
            otro = otro + 1
        posicion=posicion+1
    print("a-->",a,"  e-->",e,"  i-->",i,"  o-->",o,"  u-->",u,"  otros caracateres-->",otro)

cuenta_vocales()