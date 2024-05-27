# crear una lista de 5 alumnos alamacenaremos su nombre, apellido y edad
lista_alumnos=[{
        "nombre":"abel",
        "apellido":"rojas",
        "edad":27
    },{
        "nombre":"cielo",
        "apellido":"castro",
        "edad":23
    },{
        "nombre":"ruth",
        "apellido":"castillo",
        "edad":18
    },{
        "nombre":"flor",
        "apellido":"lucana",
        "edad":18
    },{
        "nombre":"rocio",
        "apellido":"lobo",
        "edad":25
}]
# insertar al final de la lista los datos de antoni
lista_alumnos.append({
    "nombre":"antoni",
    "apellido":"cuevas",
    "edad":25
})
print(lista_alumnos)
# eliminar de la lista si existe los datos de abel
lista_alumnos.remove({
    "nombre":"abel",
    "apellido":"rojas",
    "edad":27
})
print(lista_alumnos)
# buscar y mostrar el alumno en la posicion 4 de la lista
indice=lista_alumnos.index({
    "nombre":"rocio",
    "apellido":"lobo",
    "edad":25
})
print(lista_alumnos[indice])