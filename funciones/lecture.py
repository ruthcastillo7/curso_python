# return devuelve valores que podre hacer uso
## crear una funcion que retorne el numero 10, y muestra por pantalla si es par
### siempre que el valor que retorne mi funcion se utilice en mas sentencias u operaciones 
# de return
# def diez():
#     return 10
# if diez()%2==0:
#     print("es par")
# else:
#     print("es inpar")
# # print solo muestra por terminal

# #12/06/2024
# # return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estructurado
# # crear una funcion que me muestre el producto de dos numeros
# def producto (a,b):
#     return a*b
# ## su ejecucion:
# print(producto(4,8))

# #crear una funcion que me retorne una lista de tre numeros
# def lista_numeros():
#     return [3,2,6]

# # print usaremos cada vez que nuestra funcion retorne un mensaje
# # crear una funcion que por parametro reciba un nombre y retorno
# # un mensaje de bienvenida con el nombre
# def mensaje(nombre):
#     print(f"hola, [nombre], bienvenido al chongo")
# ## para su ejecucion
# mensaje("jose")


# 1. crear una funcion que reciba por lista de numeros y me devuelva el
# # numero menor, mostrar para terminal el valor retornado por la funcion
# lista=[4,3,6,78,7]
# def Min(l):
#     minimo=l[0]
#     for n in l:
#         if n < minimo:
#             minimo=n
#         return minimo
# print(Min(lista))
# # 2. Crear una funcion que reciba como parametro el nombre y la edad de una persona
# # mi funcion debera retornar un diccionario con los datos, luego mostrar por
# # terminal el valor de retorno de mi funcion
# nom=input("ingrese su nombre: ")
# edad=int(input("ingrese su edad: "))
# def persona(nom,edad):
#     # return {
#     #     "nombre":nom,
#     #     "edad":edad
#     #     }
#     return dict(
#         nombre=nom,
#         edad=edad
#     )
# print(persona(nombre,edad))


#17/06/2024
# #esto es un argumento posisional
# def num_pares(*args):
#     lista_pares=[]
#     for n in args:
#         if n%2==0:
#             lista_pares.append(n)
#     return lista_pares
# #por comprencion
# #return [n for n in args if n%2==0]
# print(num_pares(8,5,4,7,9,25,4,7,12)) #[8, 4, 4, 12]

# #empaquetado y desempaquetado de argumento nominales
# def alumnos(**kwargs):
#     kwargs["nombre"]="abel"
#     print(kwargs)
# alumnos(nombre="miguel",apellido="largo",edad=30) #'nombre':'miguel','apellido':'largo','edad':'30'}

##24/06/2024
## Ejercicios de lambda
# saludo=lambda:"hola"
# print(saludo())

# saludo=lambda n,a:f"hola, {n, {a}"
# print(saludo("ruth","castillo"))

#crear un programa anonimo que reciba como parametro
#una lista de 5 numerros y retorne dos listas
# una con los numeros pares y otra con numeros impares

# #forma 1:
# lista=[1,2,3,4,5,47,7,10,8]
# pares=lambda l:[n for in lista if n%2==0]
# impares=lambda l:[n for in lista if n%2!=0]
# print(pares(lista))
# print(impares(lista))

# forma 2: usar diccionario por comprecion TAREA
lista=[1,2,3,4,5,47,7,10,8]
pares=lambda l:[n for n in lista if n%2==0] 
impares=lambda l:[n for n in lista if n%2!=0]
print(pares(lista))
print(impares(lista))

#funcion callnback
def mensaje(m):
    print(m)
def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())