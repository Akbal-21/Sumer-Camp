
ano=int(input("Ingrese un año: "))

if ano%400==0 or ano%4==0:
    print("Es un año bisiesto")
else:
    print("No es un año bisisesto")