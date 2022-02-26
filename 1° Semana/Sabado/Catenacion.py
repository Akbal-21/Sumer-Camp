
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

print("Hola " + nombre.capitalize() + " " + apellido.capitalize())

print("Hola {} {}".format(nombre.capitalize(), apellido.capitalize()))

print("Hola {0} {1}".format(nombre.capitalize(), apellido.capitalize()))
print("Hola {1} {0}".format(nombre.capitalize(), apellido.capitalize()))

print(f"Hola {nombre.capitalize()} {apellido.capitalize()}")
