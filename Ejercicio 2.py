# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de
# ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un
# mensaje por pantalla informando de ello.

def tabla_multiplicar(n):
    if n in range(1,11):
        nombre_fichero = 'tabla-' + str(n) + '.txt'
        fichero = open(nombre_fichero, 'r')
        print(fichero.read())
    else:
        print("No existe ese fichero.")
    return
n = int(input("Escriba un número del 1 al 10: "))
n = tabla_multiplicar(n)

