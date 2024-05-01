#4. Validar si un número ingresado por el usuario es primo o no.
#ingresar numero usuario
numero_usuario:int=int(input("ingrese numero: "))
if numero_usuario %2==0:
	print("no es primo")
if numero_usuario %2==1:
	print("si es primo")
	


#3. Validar si un número ingresado por el usuario es positivo, negativo o cero.
ingrese_numero:int=int(input("ingrese numero:"))
#usamos los operadores de comparacion
print("numero ingresado es positivo:", ingrese_numero>=0)
print("numero ingresado es negativo:", ingrese_numero<0)
print("numero ingresado es 0:", ingrese_numero==0)
#comparamos el valor usamos bool
#comparacion:bool=ingrese_numero >= 0 and ingrese_numero < 0

#2. Determinar si un año ingresado por el usuario es anterior al año actual.
#ingrese año usuario
año_del_usuario:int=int(input("ingrese año: "))
#ingrese año actual
año_actual=2024
#determinar año anterior usando operadores de comparacion
mensaje=año_del_usuario < año_actual
print("¿es TRUE o FALSE que el año introducido es anterior al actual?")
print(mensaje)


#5. Determinar si un número ingresado por el usuario es par y mayor que 10.
numero_usuario:int=int(input("ingrese numero: "))
#imprimimos segun lo que pide
print("numero ingresado es par:", numero_usuario %2==0)
print("numero ingresado es impar:", numero_usuario %2==1)
print("numero ingresado mayor que 10:", numero_usuario>10)
print("numero ingresado manor que 10:", numero_usuario<10)
