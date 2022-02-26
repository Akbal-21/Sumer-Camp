
NUM = 5  # en mayusculas por ser constante

es_correcto = False  # esto es una bandera

while es_correcto==False: #while not es_correcto:   es otra forma 
    adiv = int(input("Ingresa un numero: "))
    if adiv == NUM:
        es_correcto = True
        print("Adivinaste")
    else:
        print("No adivinaste")


#Crear un do while
adiv1 = int(input("Ingresa un numero: "))

while adiv1!=NUM:
    print("No adivinaste")
    adiv1 = int(input("Ingresa un numero: "))
print("Adivinaste")