# TIPOS DE DATOS ESTRUCTURADOS (TDA - TIPOS DE DATOS ABSTRACTOS)
``` python
#listas []
## sus valores o elementos se pueden actualizar o eliminar
## tanto listas con o las tuplas todos los elementos que se crean python crea indices (negativo y positivo)
lista=["nombre",20,2,3,False,["texto,.2"]]

#tupla ()
## sus valores o elementos no pueden ser modificados o eliminados
### la lista que esta dentro de una tupla no puede modificarse
## tanto listas con o las tuplas todos los elementos que se crean python crea indices (negativo y positivo)
tupla=("ruth",20,2,3,False,[])

#diccionarios {} (en yava se conoce como OBJETOS)
## los diccionarioas almacenan los datos con clave:valor
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
- [!TIP]
- **Observacion:** que los tipos de datos estructurados pueden almacenar enm su interior otros tipos de datos estructuarados

``` python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20,
        "amigos":[no tiene]
    },{
        "nombre":"ruth",
        "edad":13,
        "amigos":["flor","rocio"]
    },{
        "nombre":"jose ma",
        "edad":80,
     },{
        "nombre":"ronny",
        "edad":18,
    }
    
    ]
    #terminar de copiar
```

## Metodos
### 1. Convertir texto a lista
``` python
#Metodo list
texto="hola"
list(texto) #["h","o","l","a"]

# 1. Metodo split
#separa cada caracter de la lista
texto="hola como estan,alumnitos lindos"
texto.split(",")
#los elementos se separan por comas
#trocea textos en listas a partir de un limitador (espacios, comas ",") o sea: *"hola como estan*  es uno y el otro es *alumnitos lindos"*, porque el limiytador es una coma ",", es depende de cada uno los indicadores    que ponemos

# 2. Metodo join
texto_largo="este es un texto largo chiquita y chiquito"
nuevo_texto=texto_largo.split(" ") #aqui se separa cada palabra en lista []
print(" ".join(nuevo_texto)) #aqui indicamos con que indicador uniremos las palabras
```
### 2. Agregar elementos a una lista
``` python
# 1. Metodo append - es el metodo que me permite agregar elementos alñ final de una lista
# en jaya se le coonoce como git "push" (o sea sube a la nuve)
lista=["hola"]
lista.append("mundo")
print(lista) #["hola","mundo"]

# 2. Metodo insert - es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista
#parametros: 1. indice o posision en la que agregare el texto (0) y 2. texto que voy a agregar "texto"
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0:"rocio") #["rocio","edith","ruth","luz"]

# 3. Metodo pop - es el metodo que elimine el ultimo elemento de una lista, es lo contrario a append.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop() #["edith","ruth"]

# Primera opcion - Metodo remove - este metodo elimine el por el nombre el elememto que coincida dentro de mi lista
#elimina por nombre o texto
lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# Segunda opcion - Metodo pop - al pasarle por parametro un indice este lo eliminara de la lista
#elimina por indice
#si a pop no le especificas un indice por defecto elimina el ultimo
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)

#4. Buscar un elemento en una lista .index (se usa para informacion grande)
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombre[indice])

pertenencia="edith" in lista_nombres #True False
```

29/05/2024
# Tipos de datos estructurados (TDA - Tipos de datos)
## Metodos
### 5.Comparacion de listas
podemos hacer uso de los operadores de comparaciom para comparar listas
**Ejem:**
``` python
compara=[1,2,3]<[1,2,3]
# 1 no porque son iguales en amabas listas
# 2 no porque son iguales iguales en ambas listas
# 3 evalua que menor a 4
#entonces la primera lista es menor que la segunda lista
print(compara) 
```

### 6. cuidado con las copias

### 7. FE DE ERRATAS (Actualizar listas)
``` python
lista=[1,3,4,5,6]
copia_lista=lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
#modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
       "edad":15 
    },
    {
        "nombre":"anthony"
        "eada":29
    }
]
#clave que quiero actualizar [0]["edad"]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
#lo crea en el print que hago
print(alumnos)

### 05/06/2024
### 7. Listas y diccionarios por comparacion: es una tecnica pythonica que nos permita
### crear listas y diccionarios en una sola linea combinando bucles y deciciones.

>[!NOTE] 
>**vlc** value loop condicion - valor bucle condicion

# lista por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n)for n in texto.split(",") if int (n)%2==0 ]            
print(nueva_lista)
# diccionarios por comprencion
lista_amigos=["abel","antony","edith","ruth"]
diccionarios={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)
