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
oracion:str=input("escriba una oracion con comas: ")
#contador:int=0
for i,l in enumerate(oracion):
    if l==",":
        print("soy una coma")
#    contador=contador+1
#print(f"la cantidad de comas que tengo es {contador}")