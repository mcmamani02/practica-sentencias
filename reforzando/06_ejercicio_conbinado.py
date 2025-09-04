
contactos=[]
continuar="si"
#agregar contactos
while continuar=="si":
    nombre=input("Ingrese nombre: ")
    telefono=input("Ingrese su telefono: ")
    nuevo_contacto={"Nombre":nombre,"Telefono":telefono}
    contactos.append(nuevo_contacto)
    continuar=input("desea continuar? ")
#mostrar contactos
print (contactos)
#buscar contacto
buscar_contacto=input("ingresa un nombre:")
for contacto in contactos:
    if buscar_contacto==contacto["Nombre"]:
        print(contacto)