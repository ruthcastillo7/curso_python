#escribir un programa que pregunte al usuario su edad y muestre por pantalla
#si es mayor de edad o no.
# ingrese_edad:int=int(input("ingrese edad usuario: "))
# if ingrese_edad >= 18:
#     print("eres mayor de edad")
# if ingrese_edad < 18:
#     print("eres menor de edad")
# #escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# #pregunte al usuario por la contraseña e
# #imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
# #sin tener en cuenta mayusculas y minusculas.
# guardada_variable="Ruthcashu22"
# contraseña:str=input("ingrese contraseña: ")
# if paswor == contraseña:
#     print("contraseña correscta")
# else:
#     print("contraseña correcta")
# #escribir un programa que pida al usuario un numero entero positivo y muestre por
# #pantalla la cuenta atras desde ese numero hasta cero separados por comas.
# usuario:int=int(input("ingrese numero positivo: "))
# resultado=""
# for i in range(usuario;-1,-1):
#     resultado += str(i)
#     if i >0:
#         resultado += ","
# print(resultado)

#SEMANA 07:
#CREAR UN PROGRAMA QUE ME MUESTRA LA TABLA DE MULTIPLICAR DE 1 HASTA 5
# for i in range(1,6):
#     print(f"la tabla de (i)")
#     for j in range(1,13):
#         resultado=i*j
#         print(f"{i}x{j}={resultado}")
#CREAR UN PROGRAMA QUE PIDA UN NUMERO Y QUE MUESTRA LA TABLA DE MULTIPLICAR DE ESE NUMERO
usuario:str=int(input("ingrese un numero: "))
print(f"la tabla del {usuario}")
for n in range(1,13):
    print(f"{usuario}x{n}={usuario*n}")