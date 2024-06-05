# crear una lista de 5 alumnos alamacenaremos su nombre, apellido y edad
# lista_alumnos=[{
#         "nombre":"abel",
#         "apellido":"rojas",
#         "edad":27
#     },{
#         "nombre":"cielo",
#         "apellido":"castro",
#         "edad":23
#     },{
#         "nombre":"ruth",
#         "apellido":"castillo",
#         "edad":18
#     },{
#         "nombre":"flor",
#         "apellido":"lucana",
#         "edad":18
#     },{
#         "nombre":"rocio",
#         "apellido":"lobo",
#         "edad":25
# }]
# # insertar al final de la lista los datos de antoni
# lista_alumnos.append({
#     "nombre":"antoni",
#     "apellido":"cuevas",
#     "edad":25
# })
# print(lista_alumnos)
# # eliminar de la lista si existe los datos de abel
# lista_alumnos.remove({
#     "nombre":"abel",
#     "apellido":"rojas",
#     "edad":27
# })
# print(lista_alumnos)
# # buscar y mostrar el alumno en la posicion 4 de la lista
# indice=lista_alumnos.index({
#     "nombre":"rocio",
#     "apellido":"lobo",
#     "edad":25
# })
# print(lista_alumnos[indice])


# 2. crear una lista con 4 diccionarios donde tendran los datos
#de sus mascotas (nombre, edad, sexo, raza)

# mascotas=[
# {
# "nombre":"yuki",
# "edad":12,
# "sexo":"hembra",
# "raza":"poodle"
# },{
# "nombre":"hashiko",
# "edad":25,
# "sexo":"macho",
# "raza":"golden retriever"
# },{
# "nombre":"shiroku",
# "edad":21,
# "sexo":"macho",
# "raza":"husky"
# },{
# "nombre":"valky",
# "edad":12,
# "sexo":"hembra",
# "raza":"chihuahua"
# }]
# # tareas:
# # mostrar la lista con los 4 diccionarios
# print(mascotas)
# # editar el 3er registro y cambiarle la edad sin modificar la lista original
# mascotas[2]["edad"]=19
# #print(mascotas)
# # mostrar la lista original y luego la lista con el 3er registro modificado
# copia_mascotas=mascotas.copy()
# print(copia_mascotas)


# 03/05/2024
# 1. un empresario de alquiler de motos desea guardar en una base de datos
# la informacion de sus vehiculos, proceso que desea automatizar con un sistema
# informatico, las acciones que puede realizar el empresario son ver la lista de autos
# que tiene, podra tambien actualizar la lista y agregar un nuevo veiculo

### casos de uso
## como: empresario
## quiero: guardar la informacion del alquiler de mis veiculos en una base de datos
## para: automatizar el sistenma de acciones de mi empresa

## como: empresario
## quiero: ver y agregar nuevos autos si hacen falta
## para: tener una informacion actualizada por cada cambio que realice


### programacion

## como: empresario
## quiero: guardar la informacion del alquiler de mis veiculos en una base de datos
## para: automatizar el sistenma de acciones
# autos=[
# {
# "marca":"toyota",
# "color":"negro",
# "precio/alquiler":10000
# },{ 
# "marca":"susuki",
# "color":"plomo",
# "precio/alquiler":12000
# },{ 
# "marca":"bentley",
# "color":"rojo", 
# "precio/alquiler":13000
# },{ 
# "marca":"arpsun",
# "color":"verde",
# "precio/alquiler":20000
# },{ 
# "marca":"honda",
# "color":"blanco",
# "precio/alquiler":14000
# }]

# ## como: empresario
# ## quiero: ver y agregar nuevos autos si hacen falta
# ## para: tener una informacion actualizada por cada cambio que realice
# copia_autos=autos.copy()
# print(copia_autos)

# autos.append({
#     "marca":"subaru",
# "color":"negro/blanco",
# "precio/alquiler":11000
# })
# print(autos)

# 05/06/2024
# crear una lista de los primeros 20 numeros primos haciendo uso de comprencion
# numeros=[2,50]
# num_primos=[n for n in range(2,40) if numeros if n%2==1 ]
# print(num_primos)
numeros_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if num != i)]
los_20_primos = [num for num in numeros_primos][:20]
print(los_20_primos)

# numeros=[2,50]
# num_primos=[n for n in range(2,40) if numeros if n%2==1 ]
# print(num_primos)