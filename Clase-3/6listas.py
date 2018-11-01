import os
import sys


def sumadearr_lista(arr, dict):
    result1 = 0
    result2 = 0
    for i in dict.keys():
        result1 += dict[i]
    for a in range(len(arr)):
        result2 += arr[a]
    return result1 + result2

def sumadelist(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result

def sumadelista_int(arr,int):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result + int

def sumadict(dict):
    result = 0
    for key in dict.keys():
        result += dict[key]
    return result

def sumaacum(arr):
    result = 0
    arr2 = []
    for i in arr:
        result += i
        arr2.append(result)
    return arr2

def elimina(arr):
    if len(arr) > 2:
        del arr[0]
        del arr[-1]
    else:
        print("Necesito un arreglo de más de 1 posición")
    return arr

def duplicados(arr):
    return set(arr)



dict = {'a':4, 'b':5, 'c':6, 'd':7}
arr = [5,3,1,6,7,8,5,8,1]
int = 1
a = sumadearr_lista(arr, dict)
b = sumadelist(arr)
c = sumadelista_int(arr,int)
d = sumadict(dict)
e = sumaacum(arr)
f = elimina(arr)
d = duplicados(arr)

print(d)
