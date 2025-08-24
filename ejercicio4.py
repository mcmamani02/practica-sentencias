nombres=["Maria", "Juan", "Bruno"]#lista es igual a array
print(nombres)
nombres.append("Hernan")
cant_nombres=len(nombres) #len me da la cantidad de items de la lista
print(str(cant_nombres))
#for nombre in nombres:
  #  print(nombre)
    
count=0
while count < cant_nombres:
    print(nombres[count])
    count+=1
    