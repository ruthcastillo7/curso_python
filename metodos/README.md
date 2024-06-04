# METODOS EN PYTHON
## NUMERO
```PYTHON
len(1234567)
# devuelve 1 cantidad de digitos
# 6

int=int(input("variable: "))
# INPUT almacena la informacion de una variable ya sea numero, texto, etc.
# pero siempre se define si es int=int() o srt=int()

int.from_bytes()
>>> int.from_bytes(b'4f2','little') #3302964
# from_bytes	Devuelve el entero representado por un array de bytes.

int.real
>>> (4).real #4
# from_bytes	Devuelve el entero representado por un array de bytes.
```
## TEXTO
```PYTHON
len("hola mundo")
# devuelve la cantidad de caracteres
# el espacio cuernta tambien como un caracter
# 10

str=str(input("variable: "))
# INPUT almacena la informacion de una variable ya sea numero, texto, etc.
# pero siempre se define si es str=str() o srt=int()

str.join(iterable)
# une todos los elementos de una iteracion con un especifico str
print("y".join(["a","b","c"])) # a y b y c

```
## LISTAS
```PYTHON
len(["h","o","l","a"])
# devuelve cantidad de elemntos ("elemento" es lo que esta dentro de array)
# el espacio cuenta tanmbien comoun caracter
#4

tienda=["manzana","banana","fresa","orange"]
tienda.clear()
#elimina todos los elementos de la lista

tienda=["manzana","banana","fresa","orange"]
tienda.copy()
# devuelve una copia de la lista especificada

numeros=[1,1,2,3,3,3,3,3]
numeros.count(3) # 5
# devuelve la cantidad de veces de un numero que esta dentro de una lista

numeros=[1,2,3,4,5,6,7]
numeros.index(3)
# Buscar un elemento en una lista .index (se usa para informacion grande)

lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0:"rocio") #["rocio","edith","ruth","luz"]
# agrega elementos en la ubicacion que asignes

tienda=["manzana","banana","fresa","orange"]
tienda.append("atun")
# añade elemtos al final de la lista

lista_nombres=["edith","ruth","luz"]
lista_nombres.pop() #["edith","ruth"]
#elimina el ultimo elemnto de una lista

lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")
# elimina un elemento de una lista segun le asigne
```
## TUPLAS
```PYTHON
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
# El count()método devuelve el número de veces que aparece un valor específico en la tupla.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
# El index()método encuentra la primera aparición del valor especificado.
# El index()método genera una excepción si no se encuentra el valor.
```

## DICCIONARIOS
```PYTHON
autos={
"marca":"toyota",
"color":"negro",
"precio/alquiler":10000
}

variable=car.get("color")
print(variable) # "negro"
# ".get" devuelve el valor del elemento con la clave especificada

car.update("color":"negro")
print(car)
# ".update" inserta los elemntos especificados en el diccionario (deben ser objetos iterables con pares clave-valor)

car.copy()
print(car)
# ".copy" devuelve copia del diccionario especificado
```