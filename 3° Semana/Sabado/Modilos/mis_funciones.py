from datetime import datetime


def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


def get_inicial(palabra, Mayus=True):
    if Mayus:
        inicial=palabra[0].upper()
    else:
        inicial=palabra[0]
    return inicial