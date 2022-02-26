from datetime import datetime


def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = "Susan"
print_time("fisrst name assignated")

for i in range(0, 10):
    print(i)
print_time("loop completed")


# los strings son listas.

nombre = input("enter your first: ")
innombre=nombre[0:1]
apellido = input("enter your last:")
inapellido=apellido[0:1]
print(f"your initials are: {innombre} {inapellido}")


    #con parametros y return, podemos cambiar los parametros de lugar siempre y cuando tengan el mismo nombre

def get_inicial(name):
    initial=name[0:1].upper()
    return initial
    
nom = input("enter your first name: ")
innom=get_inicial(nom)

ape = input("enter your last name: ")
inape=get_inicial(ape)

print(f"your initials are: {innom} {inape}")

    #simplificación del codigo anterior pero más confuso

def get_inicial(name):
    initial=name[0:1].upper()
    return initial
    
nom = input("enter your first name: ")

ape = input("enter your last name: ")

print(f"your initials are: {get_inicial(nom)} {get_inicial(ape)}")