
# def print_full_name(a,b):
#    print(f"Hello {a} {b}! Your just delved into python.")

# if __name__ == '__main__':
#    fisrt_name=input("")
#    last_name=input("")
#    print_full_name(fisrt_name.capitalize(), last_name.capitalize())


if __name__ == '__main__':
    N = int(input())

    lista=[]
    for i in range(N):
        # con un set("  ") podemos decidir que es el separador
        comand = input("").split()
        if comand[0]=="insert":
            lista.insert(int(comand[1]), int(comand[2]))
        elif comand[0]=="print":
            print(lista)
        elif comand[0]=="remove":
            lista.remove(int(comand[1]))
        elif comand[0]=="append":
            lista.append(int(comand[1]))
        elif  comand[0]=="sort":
            lista.sort()
        elif  comand[0]=="pop":
            lista.pop()
        else:
            lista.reverse()