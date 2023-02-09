# Mediante un "while" loop, comprueba si texto que ha introducido el usuario es distinto de "S" y de "N".
# De ser así, el programa se repetirá infinitamente hasta que el usuario introduzca uno de estos dos caracteres.
print("""Para detener este programa, debe escribir "S" o "N" (en letras mayúsculas).""")
user_input = None

while user_input != "S" and user_input != "N":
    user_input = input("Introduzca un texto: ")
