
gpa = float(input("Ingrese su promedio"))
lowest_grade = float(input("Ingrese su calificacion mas baja"))


if gpa >= .85 and lowest_grade >= .70:
    honour_roll=True
else:
    honour_roll=False



#Más adelante en el código
if honour_roll:
    print("well done")
