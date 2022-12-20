# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de
# ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un
# mensaje por pantalla informando de ello.

def tabla_multiplicar(n):
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    fichero = open(nombre_fichero, 'r')
    for n in range(1,11):
        print(fichero.read())
    if n != (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        print("No existe ese fichero.")
    return
n = int(input("Escriba un número del 1 al 10: "))
n = tabla_multiplicar(n)

