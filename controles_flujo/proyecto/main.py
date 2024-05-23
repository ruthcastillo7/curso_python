grass:list=[]
reserva=f"""
____________GRASS SINTETICO__________
HORARIOS DISPONIBLES:
1. LUNES s/. 30: de 4 p.m a 5 p.m
2. MARTES s/. 30: de 4 p.m a 5 p.m
3. MIERCOLES s/. 60: de 4 p.m a 6 p.m
4. JUEVES s/. 30: de 4 p.m a 5 p.m
5. VIERNES s/. 30: de 4 p.m a 5 p.m
6. SABADO s/. 90: de 3 p.m a 6 p.m
 """

while True:
    print(reserva)
    opcion=input("Ingrese la opcion del horario que desea reservar: ")
    if opcion == "1":
        print("su recerva del dia LUNES fue exitosa🎉⚽🏀🏐")
    elif opcion == "2":
        print("su recerva del dia MARTES fue exitosa🎉⚽🏀🏐")
    elif opcion == "3":
        print("su recerva del dia MIERCOLES fue exitosa🎉⚽🏀🏐")
    elif opcion == "4":
        print("su recerva del dia JUEVES fue exitosa🎉⚽🏀🏐")
    elif opcion == "5":
        print("su recerva del dia VIERNES fue exitosa🎉⚽🏀🏐")
    elif opcion == "6":
        print("su recerva del dia SABADO fue exitosa🎉⚽🏀🏐")
    break
print("VERIFICACION:")
if opcion == "1":
        print("su recerva es para el dia LUNES a horas 4 p.m a 5 p.m y debe pagar S/. 30")
if opcion == "2":
        print("su recerva es para el dia MARTES a horas 4 p.m a 5 p.m y debe pagar S/. 30")
if opcion == "3":
        print("su recerva es para el dia MIERCOLES a horas 4 p.m a 6 p.m y debe pagar S/. 60")
if opcion == "4":
        print("su recerva es para el dia MIERCOLES a horas 4 p.m a 5 p.m y debe pagar S/. 30")
if opcion == "5":
        print("su recerva es para el dia MIERCOLES a horas 4 p.m a 5 p.m y debe pagar S/. 30")
if opcion == "6":
        print("su recerva es para el dia MIERCOLES a horas 3 p.m a 6 p.m y debe pagar S/. 90")
