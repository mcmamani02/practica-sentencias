matriz = [
    [3.3, 6.1, 4.0],
    [4.9, 5.7, 6.4]
]
fila=int(input("ingrese fila: "))
columna=int(input("ingrese columna: "))
if fila < len(matriz) and columna < len(matriz[fila]):
    print(matriz[fila][columna])
else:
    print("error fila solo tiene ", len(matriz))
    print("error columna solo tiene ", len (matriz[len(matriz)-1]))
    
#array=matriz[fila]# fila =0 matriz[fila] [3.3, 6.1, 4.0] array=[3.3, 6.1, 4.0]
#array[columna]