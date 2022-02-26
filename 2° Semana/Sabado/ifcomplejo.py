
gpa = float(input("Ingrese su promedio"))
lowest_grade = float(input("Ingrese su calificacion mas baja"))


if gpa >= .85:
    if lowest_grade >= .70:
        print("well done")

if gpa >= .85 and lowest_grade >= .70:
    print("well done")
