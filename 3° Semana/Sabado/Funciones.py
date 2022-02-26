import datetime
# from  datetime import datetime  una forma más facil de llamar funciones


def print_time():
    print("task complete")
    print(datetime.datetime.now())
    # print(datetime.now())   esto es con la importación espeífica
    print()


fist_name = "Susan"
print_time()

for i in range(0, 10):
    print(i)
print_time()
