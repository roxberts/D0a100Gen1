def sumacum(lista):
    sum=0
    nuevl=[]
    for item in lista:
        sum = sum + item
        nuevl.append(sum)
    return nuevl

def elimina(lista):
    del(lista[0])
    del(lista[-1])
    print(lista)

lista=[1,2,3,4]
elimina(lista)
