
# si ingresa una a,e,i,o,u escribir vocal

# si ingresa una y poner que a veces es vocal
# o consonante

# de otra forma escribir que es una consonante

let = input("Ingrese una letra: ")

# clasificación y resultado

letra = let.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es vocal")
elif letra == 'y':
    print("Aveces es vocal y otras veces es consonante")
else:
    print("Es consonante")
