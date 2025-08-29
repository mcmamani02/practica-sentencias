edad=int(input("Ingrese su edad: "))
tiene_licencia=input("Tiene licencia de conducir? si/no: ")
tiene_licencia=tiene_licencia=="si"
if edad>=18:
    print("Puede conducir")
elif edad>=18:
    print("debe sacar la licencia")
else:
    print("es menor de edad")