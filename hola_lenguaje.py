import os

nombre = os.getenv('USERNAME')
lenguaje = os.getenv('LANGUAGE')

print(f"Hola {nombre}, tu lenguaje favorito es {lenguaje}")
