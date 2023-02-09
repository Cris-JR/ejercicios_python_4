# Mediante la definición de una función, se comprueba si un número introducido por el usuario es primo o no.
# Para ello, se emplea un "for" loop que comprueba si el resto de dividir ese número entre los de un determinado rango,
# da como resultado 0 o no.
# Finalmente, se ejecuta la función pasando como argumento el número introducido por el usuario.
user_input = int(input("Inserte un número para comprobar si es primo o no: "))


def es_primo(numero):
    no_es_primo = None

    if numero == 1:
        no_es_primo = True
    elif numero > 1:
        for value in range(2, numero):
            if numero % value == 0:
                no_es_primo = True
                break

    if no_es_primo:
        print(f"El número {numero} NO es primo.")
    else:
        print(f"El número {numero} sí es primo")


es_primo(user_input)
