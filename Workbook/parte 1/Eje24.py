# Ejercicio 24: unidades de tiempo(22 líneas)
# Cree un programa que lea una duración del usuario como un número de días, horas,
# minutos y segundos. Calcule y muestre el número total de segundos representados
# por esta duración

dia = int(input("Ingrese un numero de dias: "))
horas = int(input("Ingrese un numero de horas: "))
minutos = int(input("Ingrese un numero de minutos: "))
segundos = int(input("Ingrese un numero de segundos: "))
print("\n")
horas += (dia*24)

print(f"Horas: {horas}")

minutos += (horas*60)

print(f"Minutos: {minutos}")

segundos += (minutos*60)

print(f"Segundos: {segundos}")
