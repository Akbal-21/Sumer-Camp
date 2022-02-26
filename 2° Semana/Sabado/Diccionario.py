
# no hay orden garantizado en los diccionarios
person = {"first": "Chistopher"}  # se crea el diccionario y puede esta vacio
person["last"] = "Harrison"  # agregar datos al diccionario

Perso = {"first": "Fernando", "last": "Serrano"}


print(person)

print(person["first"])  # acceder al dato por llave


'''
tuples: son inmutables, almacena una relacion de datos y no se modifican
    srudenr=("Maria",8,4.5)

sets: almacena datos unmutables y un dato solo puede estar una vez
    set vacio
    empty_set=set{}
    set con datos
    new_set={"Maria","Carlos"}
'''
#Diccionarios en listas

persona=[person,Perso]

print(persona)
print()
print(persona[1])
print()
print(persona[1]["first"])
