grass:list=[]
reserva=f"""
____________GRASS SINTETICO__________
HORARIOS DISPONIBLES:
1. LUNES s/. 30: de 4 p.m a 5 p.m
2. MARTES s/. 30: de 4 p.m a 5 p.m
3. MIERCOLES s/. 60: de 4 p.m a 6 p.m
4. JUEVES s/. 30: de 4 p.m a 5 p.m
5. VIERNES s/. 30: de 4 p.m a 5 p.m
6. SABADO s/. 90: de 3 p.m a 3 p.m
 """
while True:
    print(reserva)
    opcion=input("Ingrese la opcion del horario que desea reservar: ")
    if opcion == "1":
        print("su recerva fue exitosa, pague s/. 30")
    elif opcion == "2":
        print("su recerva fue exitosa, pague s/. 30")
    elif opcion == "3":
        print("su recerva fue exitosa, pague s/. 60")
    elif opcion == "4":
        print("su recerva fue exitosa, pague s/. 30")
    elif opcion == "5":
        print("su recerva fue exitosa, pague s/. 30")
    elif opcion == "6":
        print("su recerva fue exitosa, pague s/. 90")
        break

# PRECIOS=f"""
#  1. el precio para el dia lunes es: s/. 30
#  2. el precio para el dia martes es: s/. 30
#  3. el precio para el dia miercoles es: s/. 60
#  4. el precio para el dia jueves es: s/. 30
#  5. el precio para el dia viernes es: s/. 30
#  6. el precio para el dia sabado es: s/. 90"""
# # print(f"""VERIFICACION:
#       SU RESERVA ES DEL DIA {OPCION} ASI UE PAGUE {PRECIO}""")