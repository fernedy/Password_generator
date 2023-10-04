import random

letras_low = "abcdefghijklmnopqrstuvwxyz"
letras_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres = "!@#$%^&*-_+=<>?/|()[]{}:;,'"


def crear_password(longitud):
    todo = letras_low + letras_upper + caracteres
    passwd = ""

    for i in range(longitud):
        passwd += random.choice(todo)

    return passwd


nuevo_pass = crear_password(10)

print(nuevo_pass)
