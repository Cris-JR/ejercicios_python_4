# Este programa crea una lista vacía a la que se añaden 5 números por parte del usuario.
# Después, imprime la suma de los 5 números insertados.
lista_de_numeros = []

for value in range(5):
    lista_de_numeros.append(int(input("Por favor inserte un número: ")))

print(f"La suma de los 5 números que ha insertado da como resultado: {sum(lista_de_numeros)}")
