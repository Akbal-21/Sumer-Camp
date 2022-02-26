
L1 = float(input("Ingrese la longitud del lado uno: "))
L2 = float(input("Ingrese la longitud del lado dos: "))
L3 = float(input("Ingrese la longitud del lado tres: "))


# if L1==L2 and L2==L3:

if L1 == L2 == L3:
    nom_trin = "equilatero"
elif L1 == L2 or L2 == L3 or L1 == L3:
    nom_trin = "isoceles"
else:
    nom_trin = "escaleno"

print(f"El triangulo es {nom_trin}")
