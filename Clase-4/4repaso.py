import os
import sys

def serepite(tupla, num): #Recibe tupla y numero, si se repite numero retorna cuantas veces, si no, retorna 0
    if tupla.count(num) <= 1:
        print('0')
    else:
        print(str(tupla.count(num)))

def regresamaymen(tupla):
    print(max(tupla),min(tupla))

def regresamaymenDif(tupla):
	mayor = 0
	menor = tupla[0]
	for i in range(len(tupla)):
		if tupla[i] > mayor:
			mayor = tupla[i]
		pass
		if tupla[i] < menor:
			menor = tupla[i]
		pass
	return(mayor, menor)
	pass

def creaagenda():
    dict = {}
    nombre = input("Ingresa un nombre: ")
    telefono = int(input("Ingresa el telefono: "))
    while telefono != 0:
        dict[nombre] = telefono
        nombre = input("Ingresa un nombre: ")
        telefono = int(input("Ingresa el telefono: "))
    print(dict)

def directorio():
	agenda = {'nombre': [], 'telefono' : []}
	nom = []
	tel = []
	nom = input("Dame un nombre")
	tel = input("Dame un numero")
	while nom != '0'or tel != '0' :
		agenda['nombre'].append(nom)
		agenda['telefono'].append(tel)
		nom = input("Dame un nombre")
		tel = input("Dame un numero")
	print (agenda)

def tupladefinida():
    tupladefinida = (1,"hola", [1,2], (1,2))
    num = int(input('Dame un entero: '))
    print(tupladefinida[num])

def cosapolitica(tupla):
    for i in tupla:
        print("Estimado "+i+" vote por mi")

def propaganda(tup):
	for i in range(len(tup)):
		print('Estimado/a',tup[i], 'vote por mi.')

def inviertelista(lista):
    lista2 = []
    for i in reversed(lista):
        lista2.append(i)
    print(lista2)

def reverseList(ListReverse):
    NewList = ListReverse[::-1]
    print (NewList)

def domino(tupla,tupla2):
    if tupla[0] in tupla2 or tupla[1] in tupla2:
        print("Si encajan")
    else:
        print("No encajan")

tuplaejercicio = (1,1,1,2,3,4,5)
tup1 = (2,5)
tup2 = (3,5)
tup3 = (4,6)
tuplanombres = ("Hayde", "Viri", "Ali")
num = 2
listaejercicio = ["a","b","c"]
#serepite(tuplaejercicio,num)
#regresamaymen(tuplaejercicio)
#creaagenda()
#directorio()
#tupladefinida()
#cosapolitica(tuplanombres)
#propaganda(tuplanombres)
#reverseList(listaejercicio)
#domino(tup1, tup2)
#domino(tup2, tup3)
