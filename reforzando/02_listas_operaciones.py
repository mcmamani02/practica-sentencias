numeros = [3, 7, 2, 8, 5]
num_mayor=0
num_menor=numeros[0]
suma=0
numeros_pares=[]
#recorrer la lista 
for numero in numeros:
    if numero>num_mayor:
        num_mayor=numero
    if numero<num_menor:
        num_menor=numero
    suma+=numero
    resto=numero%2
    if resto==0:
        numeros_pares.append(numero)
  
  
print("Lista original: ", numeros)  
print("El numero mayor es: ",num_mayor)
print("El numero menor es: ",num_menor)
print("La suma de la lista es igual a: ",suma)
print("Lista de numeros pares: ", numeros_pares)
numeros.sort()
print(numeros)  

#comparar