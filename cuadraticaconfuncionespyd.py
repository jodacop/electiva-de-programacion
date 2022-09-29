def cuadraticapos(a,b,c):
  raisdenp = ((b**2) - (4 * a * c))**0.5
  resultadop = (b + raisdenp) / (2 * a)
  return resultadop

def cuadraticaneg(a,b,c):
  raisdenp = ((b**2) - (4 * a * c))**0.5
  resultadop = (b - raisdenp) / (2 * a)
  return resultadop

def imprecion(a,b,c):
  print("el resultado 1 es: x=", cuadraticapos(a,b,c))
  print("el resultado 2 es: x=", cuadraticaneg(a,b,c))

def cambio():
    print("desea cambiar algun valor? si->1, no->cualquier otro numero")
    cambiar = int(input())
    return cambiar

def main():
 print("--tomando en cuenta la ecuacion cuadratica--")
 print("-- a(x^2) + b(x) + c = 0 --")

 print("-- ingrese los valores de: a --")
 a = float(input())

 print("-- ingrese los valores de: b --")
 b = float(input())

 print("-- ingrese los valores de: c --")
 c = float(input())

 imprecion(a,b,c)
 cambiar = cambio()

 while cambiar == 1:
    print("que valor decea cambiar? a->1, b->2, c->3")
    vcambio = int(input())
    if vcambio == 1:
        print("ingrese el nuevo valor de a")
        a = float(input())
        imprecion(a,b,c)
    elif vcambio == 2:
        print("ingrese el nuevo valor de b")
        b = float(input())
        imprecion(a,b,c)
    elif vcambio == 3:
        print("ingrese el nuevo valor de c")
        c = float(input())
        imprecion(a,b,c)
    else:
        print("gracias")
    cambiar=cambio()
main()