usuarios=[
    {
        "nombre": "Maribel", 
        "edad": 30,
        "mail": "mari@gmail.com"
    },
    {
        "nombre": "Hernan", 
        "edad": 30,
        "mail": "hernan@gmail.com"  
    },
    {
        "nombre": "Luan", 
        "edad": 9,
        "mail": "luan@gmail.com"
    }
]
for usuario in usuarios:
    print(usuario["nombre"], usuario["edad"])
    
usuarios.append({
        "nombre": "Martina", 
        "edad": 10,
        "mail": "martina@gmail.com"
})
nombre=input("ingrese un nombre: ")
for usuario in usuarios:
    if nombre==usuario["nombre"]:
        print(usuario["mail"])
    