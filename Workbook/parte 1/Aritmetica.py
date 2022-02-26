
import math

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo nuemro: "))

# • La suma de a y b
ope = a+b
print(f"La suma es: {ope}")

# • La diferencia cuando b se resta de a
ope = b-a
print(f"La resta es: {ope}")

# • El producto de a y b
ope = a*b
print(f"El producto es: {ope}")

# • El cociente cuando a se divide por b
ope = (a**2)/b
print(f"El coeciente es: {round(ope,4)}")

# • El resultado de log10 a
ope = math.log10(a)
print(f"El logaritmo de a es: {round(ope,4)}")

# • The result of a**B
ope = a**b
print(f"El resultado de a^b es: {ope}")
