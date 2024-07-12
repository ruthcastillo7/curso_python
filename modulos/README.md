# AVERIGUAR SOBRE MODULOS Y PAQUETES EN PYTHON
## MODULOS
El modulo esta dentro del paquete y el paquete dentro de la libreria.
Son un conjunto de datos o codigos que `estan dentro de un archivo ".py" con funciones.`
Se puede acceder a este archivo mediante otro archivo colocandole un `"."`, con el objetivo de reutilizar el codigo: ejemplo
 ```python 
#1. en el primer archivo "operacines.py" escribir el codigo de las operaciones:
   def suma(a,b):
    """funcion de suma"""
#2. en el segundo archivo "lecture.py" escribir:
suma:int=operaciones.suma(7,8)
 ```
IMPORTAR OBJETOS SEPARDOS POR COMAS. Ejemplo:
```python 
from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))

# O bien, para importar todos los objetos dentro de un módulo:
from aritmetica import *
```
## PAQUETES
Es una `carpeta con una serie de archivos ".py"`, en otras palabras es una carpeta con modulos de python. Además permite tener una jerarquía con más de un nivel de subcarpetas anidadas.

Ejemplo: podemos diseñar un paquete `matematica` creando una carpeta con la siguiente estructura.
```python 
matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py
```
Tomemos en cuenta que este paquete siempre debe tener un modulo (o archivo) llamado `"__init__.py"`, para que el interprete de Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera:
```python
import matematica.aritmetica
print(matematica.aritmetica.sumar(7, 5))
#O bien de la siguiente.
from matematica import aritmetica
print(aritmetica.sumar(7, 5))
#También, esta otra:
from matematica.aritmetica import sumar
print(sumar(7, 5))
```
Al crear el paquete, su manera de importar su contenido es el siguiente:
```python 
# ya existen datos dentro de nuestros modulos y mi paquete se llama "operaciones"
from matematica.aritmatica import operaciones.suma
print(operaciones.suma(7,8))
```
# DIFERENCIA ENTRE MODULO Y PAQUETES
El módulo es un archivo que contiene funciones de Python, variables globales, etc. No es más que un archivo .py que tiene código / instrucción ejecutable de Python. Es la pieza más pequeña de software. Puede ser un conjunto de métodos o funciones para usarlo.

El paquete es un espacio de nombres que contiene múltiples módulos. Es un directorio que contiene un archivo especial __init__.py. Es una colección de módulos.
