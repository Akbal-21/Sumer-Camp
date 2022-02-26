province = input("Ingrese una ciudad: ")


if province.capitalize() in ("Alerta", "Nunavut", "Yukon"):
    tax = 0.05
elif province.capitalize() == "Ontario":
    tax = 0.13
else:
    tax = 0.15

print(tax)

print("\n\n\n")

pais = input("Ingrese su pais: ")

if pais.capitalize() == "Canada":
    province1 = input("Ingrese una ciudad: ")
    if province1.capitalize() in ("Alerta", "Nunavut", "Yukon"):
        tax = 0.05
    elif province1.capitalize() == "Ontario":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
    print("No eres de Canada y tus impuestos son de: ", end="")
print(tax)
