# lista=["abel","anthony","miguel"]
# print(lista[1:])

# diccionario={"nombre":"antonio","edad":15,"sexo":False}
# print(diccionario["nombre"])

##separa cada caracter
# texto="hola"
# lista_texto=list(texto)
# print(lista_texto)

#trocea cada letra
# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto] #la e es la iteracion que se guardara en cada bucle de texto
# print(lista_texto)

# #trocea cada palabra
# texto_largo="hola como estan bienvenidos al salon"
# nueva_lista=texto_largo.split(" ")
# print(nueva_lista)

# #si quiero de bienvenidos para la derecha
# texto_largo="hola como estan bienvenidos al salon"
# nuevo_texto=texto_largo[16:]
# nueva_lista=nuevo_texto.split(" ")
# print(nueva_lista)

# #separando con indicador "."
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split(".")
# print(nuevo_texto[-1])

# # .join() es el metodo que usamos para unir elementos de una lista
# # primero va : .join(), luego lo demnas
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split("_") #split quita el "_"
# print(" ".join(nuevo_texto)) #quiero que juntes la frase pero con espacio y no con "_"

# #quiero convertirlo en lista en bace a un espacio
# texto_largo="este es un texto largo chiquita y chiquito"
# nuevo_texto=texto_largo.split(" ") #aqui se separa cada palabra en lista []
# print(" ".join(nuevo_texto)) #aqui indicamos con que indicador uniremos las palabras

###25/05/2024
# dato primitivo
# nombre="abel"
# print(nombre)
# otro_nombre=nombre
# print(otro_nombre)

# # dato estructurado (copia referencia de la direccion de memoria)
# lista_original=[1,2,3,4]
# copia_lista=lista_original

# lista_original[-1]=15
# print(copia_lista)


# 1. crear un programa que reciva una lista desordenada
#y muestre por teminal la lista ordenada y la lista previa a ser ordenada
lista=[4,75,1,3,6,8,2]
otra_variable=lista.sort()
print(otra_variable) #[1,2,4,6,8,75]

lista=[4,75,1,3,6,8,2]
copia_lista=lista
copia_lista=lista.copy() # .copy() : copia el valor de la lista
copia_lista.sort() #.sort() : ordena una lista de mayor a menor
print(lista)
print(copia_lista)
# [4,75,1,3,6,8,2]
# [1,3,4,6,8,75]

# 05/06/2024
# 7. Crear una lista de números enteros del siguiente texto:
texto="1,4,8,9,6"
nueva_lista=[]
for n in texto.split(","):
    nueva_lista.append(int(n))
print(nueva_lista)

# Aplicando la técnica vlc valor bucle y condición.
texto="1,4,8,9,6"
nueva_lista=[int(n)for n in texto.split(",") if int (n)%2==0 ]            
print(nueva_lista)
# diccionarios por comprencion
lista_amigos=["abel","antony","edith","ruth"]
diccionarios=[]
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario) # {"abel":4,"antony":6,"edith":5,"ruth":4}
# aplicando el vlc (valor, longitud y condicion)
lista_amigos=["abel","antony","edith","ruth"]
diccionarios={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario) # {"abel":4,"antony":6,"edith":5,"ruth":4}
