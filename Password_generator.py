import secrets
import string


def crear_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password


try:
    longitud = int(input("Por favor, introduce la longitud de la contraseña deseada: "))
    nuevo_pass = crear_password(longitud)
    print(f"Tu nueva contraseña es: {nuevo_pass}")
except ValueError:
    print("Por favor, introduce un número válido para la longitud de la contraseña.")
