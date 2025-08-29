matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lista_pares=[]
print(matriz[0])

for fila in matriz:
    print(fila[1])
for fila in matriz:
    for columna in fila:
        if columna%2==0: 
            lista_pares.append(columna)
print(lista_pares)

    
