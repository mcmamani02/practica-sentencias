estudiantes=[
    [],
    [],
    []
]
promedios=[]

for estudiante in estudiantes:
    for posicion in range(1,4):
        nota_materia=int(input(f"ingrese nota de la materia {posicion}: "))
        estudiante.append(nota_materia)
    promedio=sum(estudiante)/3
    print("El promedio de este estudiante es:", promedio)
    promedios.append(promedio)
mayor_promedio=0
for promedio in promedios:
    if promedio>mayor_promedio:
        mayor_promedio=promedio
        
print("el mayor promedio es:", mayor_promedio)


        

