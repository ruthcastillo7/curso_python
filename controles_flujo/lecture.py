#ejemplo de if
#if True:
#    print("es verdad")
#else:
#    print("es falso")

#ejemplo de for
#imprimir los numeros pares
#entre 1 - 20
#for n in range(1,21):

### clase de la semana 6
#primer ejemplo if esctructurado
#edad:int=int(input("escribe tu edad: "))
#if edad>=18:
 #   print("eres mayor")
#else:
 #  print("eres menor de edad")
#segundo ejemplo if alamcenado en variable
#edad_dos:int=int(input("escribe tu edad: "))
#respuesta: str="eres mayor" if edad_dos>18 else "eres menor"
#print(respuesta)

#08/05/24
#1. crear un programa que me imprima las 5 vocales
#vocales:str="aeiou"
#for n in range(0,5):
#    print(vocales[n])

#2. crear un programa que me imprima los 8 primeros a numeros pares:
#contador=0 ##aqui el contador es global ya que esta fuera del for y
#por ello su valor cambia ya que no depenmde de for
#for n in range(1,17):
    #si contador esta en esta parte (dentro del for) el contador volvera a su valor
    #original y no cambiara ya que es local
#    if n%2==0:
#        contador+=1
#        print(f"{n} es el numero {contador}")
##   print(n if n%2==0)

#3. crear un programa que pida al usuario escribir una oracion
#y mostrar por terminal la cantidad de variable "a" que
#tiene esa oracion 
# OJO: SOLO LAS "a" MINUSCULAS

#aqui tiene indices
#oracion:str=input("escriba una oracion: ")
#contador:int=0
#for n in range(0,len(oracion)):
#    if oracion[n]=="a"
#    contador=contador+1
#    #contador+=1
#print(f"la cantidad de letras a que tengo es {contador}")

#aqui obetnermos letras
#for n in "aeiou":
#    print(n)

#permite obtebner indice y letra
#for i,l in enumerate("aeiou"):
#    print(f"el indice es {i} y la letra es {l}")

# 4. crear un programa que me cuente la cantidad de comas
#y muestre sus indices
#OJO: tiene que pedir al usuario 
# oracion:str=input("escriba una oracion con comas: ")
# contador:int=0
# for i,l in enumerate(oracion):
#     if l==",":
#         print(f"su indice es {i}")
#         contador+=1
# print(f"la cantidad de comas introducidas es {contador}")

##15_05_24
#1. Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla todos los años que a cumplido desde 1 hasta su edad actual.
## edad_usuario:int=int(input("escriba su edad: "))
# for i in range(1, edad_usuario+1):
#     print("cumple ", i, "años")

#2. crear un programa que me pida el nombre de 3 personas y
#guarde en una variable global la ultima letra de su nombre
#mostrar por pantalla la variable global con las 3 ultimas letras del nombre de cada persona.
# ultima_letra:str=""
# for _ in range(3):
#     #si no uso la variable "n" entonces se remplaza por guion bajo "_"
#     nombre:str=input("escribe tu nombre: ")
#     #ultima_letra+=nombre[-1]
#     last_letter:str=nombre[-1]
#     ultima_letra+=last_letter
#     #ultima_letra=ultima_letra+last_letter
# print(ultima_letra)

#3. crear un programa que muestre por terminal la siguiente figura:
#a
#ee
#iii
#oooo
#uuuuu
vocale:str=input(aeiou)
for i in range(vocales):
    if i=="a":
    print(i)