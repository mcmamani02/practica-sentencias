numeros = [3, 7, 2, 8, 5]
num_mayor=0
num_menor=numeros[0]
#recorrer la lista 
for numero in numeros:
    if numero>num_mayor:
        num_mayor=numero
    if numero<num_menor:
        num_menor=numero

print(num_mayor)
print(num_menor)
#comparar