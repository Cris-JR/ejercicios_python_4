# Mediante un "while" loop, el programa recoge x números que quiera escribir el usuario y los añade a una lista.
# Tras añadir cada número a la lista, suma 1 a una variable que hace de contador, para marcar cuándo debe detenerse.
# Finalmente, comprueba cuáles son el mayor y el menor número de la lista y los imprime.

numero = int(input("Por favor, introduzca un número: "))

count = 1
lista_de_numeros = []
while count <= numero:
    lista_de_numeros.append(int(input("Introduzca un número: ")))
    count += 1

print(f"El menor valor de los números que ha introducido es: {min(lista_de_numeros)}.\n"
      f"El mayor valor de los números que ha introducido es: {max(lista_de_numeros)}.")
