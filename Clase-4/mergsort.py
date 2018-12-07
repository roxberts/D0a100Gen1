
def mergeSort(array):
    print("Dividiendo ",array)
    if len(array)>1:
        mitad = len(array)//2
        izq = array[:mitad]
        der = array[mitad:]
        mergeSort(izq)
        mergeSort(der)
        i=0
        j=0
        k=0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                array[k]=izq[i]
                i=i+1
            else:
                array[k]=der[j]
                j=j+1
            k=k+1
        while i < len(izq):
            array[k]=izq[i]
            i=i+1
            k=k+1
        while j < len(der):
            array[k]=der[j]
            j=j+1
            k=k+1
    print("Merging ",array)
array = [54,26,93,17,77,31,44,55,20]
mergeSort(array)
print(array)
