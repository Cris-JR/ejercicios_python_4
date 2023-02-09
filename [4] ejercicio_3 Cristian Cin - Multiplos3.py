# El programa define una función que alberga una lista que contiene los múltiplos de 3 hasta el número deseado.
# Después, mediante un "for" loop, por cada valor presente en el intervalo entre el 1 y el número deseado,
# se llama a la función creada anteriormente y, si cumple con los requisitos, es impreso.
print("Este programa escribe los múltiplos de 3 que van desde el 1 hasta el número que usted inserte.")
numero_final = int(input("Inserte un número: "))


def es_multiplo_de_tres(number):
    multiplos_de_tres = [number * 3 for number in range(1, numero_final)]
    if number in multiplos_de_tres:
        return True


for value in range(1, numero_final):
    if es_multiplo_de_tres(value):
        print(value)
