
n = int(input("Ingresa un numero: "))
if n % 2 != 0:
    print("Weird")
elif n >= 2 or n <= 5:
    print("Not Weird")
elif n >= 6 or n <= 20:
    print("weird")
elif n > 20:
    print("Not Weird")
