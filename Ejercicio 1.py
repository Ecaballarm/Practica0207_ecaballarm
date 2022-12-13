# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
# la tabla de multiplicar de ese número, donde n es el número introducido.
def tabla_multiplicar(n):
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    fichero = open(nombre_fichero, "w")
    for numero in range(1,11):
        fichero.write(str(n) + ' * ' + str(numero) + ' = ' + str(n * numero) + '\n')
    return
n = int(input("Escriba un número del 1 al 10: "))
tabla = tabla_multiplicar(n)
