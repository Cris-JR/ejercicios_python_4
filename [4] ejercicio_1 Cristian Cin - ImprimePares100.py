# Este programa define una función que se encarga de imprimir un número únicamente si este es par.
# Después, se ejecuta la función dentro de un intervalo que va desde el número 1 hasta el 100.
def imprime_pares(number):
    while number % 2 == 0:
        print(number)
        break


for value in range(1, 101):
    imprime_pares(value)
