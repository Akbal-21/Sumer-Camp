# En este ejercicio revertirá el proceso descrito en el ejercicio anterior.(Solved—24 Lines)
# Desarrolle un programa que comience leyendo un número de segundos del usuario.
# Luego, su programa debe mostrar la cantidad de tiempo equivalente en el formulario
# D: HH: MM: SS, donde D, HH, MM y SS representan días, horas, minutos y segundos
# onds respectivamente. Las horas, minutos y segundos deben formatearse para que
# Ocupan exactamente dos dígitos, con un 0 inicial mostrado si es necesario.

segundos = int(input("Ingrese una cantidad de segundos: "))
minutos = 0
horas = 0
dias = 0

while segundos >= 60:
    segundos -= 60
    minutos += 1

while minutos >= 60:
    minutos -= 60
    horas += 1

while horas >= 24:
    horas -= 24
    dias += 1
print(f"D: {dias}, HH: {horas}, MM: {minutos}, SS: {segundos}")
