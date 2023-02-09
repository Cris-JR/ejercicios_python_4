# Este programa calcula el factorial de un número dado.
# Para lograrlo, se establece un intervalo que englobe a los números situados entre el 1 y ese número.
# Luego, se multiplica cada número de ese intervalo por una variable inicial de contenido "1".
# Finalmente, se imprime el resultado.
numero = int(input("Introduzca un número: "))

factorial = 1
if numero < 0:
    print("Lo siento, no puedo calcular el factorial de un número negativo. :(")
elif numero == 0:
    print("El factorial de 0 es: 1.")
else:
    for value in range(1, numero + 1):
        factorial *= value

    print(f"El factorial del número {numero} es: {factorial}")
