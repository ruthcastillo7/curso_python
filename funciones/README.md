# FUNCIONES
## CONCEPTO
Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos`
y produce un valor drenominado `resultado`.
> [!NOTE]
> Todos los lenguajes de programacion tiene funcions incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`)
> En programaciom una funciom es un subprograma, es una estructura que nos permite agrupar codigo y sus principales objetivos son:
> - `NO REPETIR` fragmentos de codigo
> - `reutilizar` el codigo en distintos escenarios
## Estructura de una funcion
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor de `retorno`, una vez creada la funcion podremos solicitar su ejecucion invocada la funcion por su `nombre`.
## Definir una funcion en python
para definir una funcion en python primero utilizaremos la palabre recevada def seguida por el `nombre` de la funcion. A continuacion espesificaremos los `parametros` con `()` si es una funcion sin parametros, `(a)` si es una funcion con parametros iran separadas por `,`, finalizaremos la linea con `:`, en la siguiente linea sin olvidar el identado (hace que python sepa que el codigo le pertenece), comenzara el `cuerpo` de la funcion (micro programa) que puede contener uno o mas centencias finalmente debera retornar un resultado con las palabra recervada `return`.
> [!TIP]
> como retorno tambien se puede utilizar la `funcion interna`, `print ()`, para depuracion de codigo no es recomendable usarlo en produccion, sino al final.
> 
PRINT() DENTRO DE UNA FUNCION ES UNA HERRAMINETA DE DEPURACION DE CODIGO, PARA PROVAR SI MI FUNCION ESTA CUMPLIENDO REALMENTE LA TAREA

** EJEMPLO: **
```python
def saludo():
  saludo="hola chivo"
  saludo_dos="como estas"
  return f"{saludo},{saludo_dos}"
  #print(f"{saludo},{saludo_dos}")
print(saludo())
#saludo()
```
## Invocar una funcion
Para invocar, (o llamar, ejecutar) una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```
## Retorna un valor un valor
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
> [!WARNING]
> No confundir `print()` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto y `print()` solo mostrara el literal por terminal.
**ejemplo:**

*en el archivo `lecture.py`
## Retornando multiples valores
El secreto es hacerlo mediante un tipo de dato estructurado
```python
def tupla():
    return 2,3,4
varios()
#retorna (2,3,4)

def lista():
    return ["hola",45]
    lista()
#retorna ["hola",45]

def dicc():
    return ("nombre":"jose","edad":45)
dicc()
#retorna ("nombre":"jose","edad":45)
```

### 12/06/2024
## Parametros y argumentos
si una funcion no dispuciera de valores de entrada estaria limitada en su actuacion
es por ello que los `parametros` nos permiten variar los datos que consume una funcion para obtener distintos resultados.
**Ejemplo**
*crear una funcion que recibe un valor numerico y retorno su raiz cuadrada*
```python
def ssqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
Cuando llamamos a una funcion con `argumrntos`, los valores de estos argumentos se copian en los correspondiente `parametros` dentro de la funcion.
```python
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```

### Argumentos nominales
En esta  aproximacion los argumerntos no son copiados en unn orden especificado sino que **se asignn por nombre a cada parametro**. Ello nos permiete evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion.
para utilizarlo basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una
    frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
build_cpu(num_core=4,familia="intel",frecuencia=2.7)
```
### Argumentos posicionales
Los argumentos son copiados en in orden especifico, en este caso denemos conocer o re4cordar cual es el orden de los parametros
**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una
    frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos pocicionales
build_cpu("intel",4,2.7)
```
### Parametros por defecto
Es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que nos se proporcione un valor en el argumento en la llamada o ejecucion a la funcion, el parametro correspondiente tomara el  valor definido  por defecto.
**Ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):
alumnos("ruth","castillo")
alumnos("anthony","crucez","desaprobado")
```


### Desempaquetado/Empaquetado de argumentos (tarea) 17/06/2024
## EMPAQUETADO DE ARGUMENTOS

Consiste en escribir un conjunto de datos (en este caso las tuplas) dentro de una variable. *Ejemplo:*
python
#1:
```python
edades=(10,20,30,40,50)
print(type(edades))
# <<class "tupla">

#2:
alturas=1.76,1.68,1.87,1.65,1.90
print(type(alturas))
# <<class "tupla">


En ambos casos son tuplas y ya están empaquetadas, también podemos empaquetarlas de la siguiente manera: *Ejemplo:*
python
x=345
y=656
z=777
variable=x,y,z
print(variable)
#(345,656,777)


## DESEMPAQUETADO DE ARGUMENTOS

En este caso hacemos todo lo contrario de lo anterior, en vez de empaquetar, nosotros desempaquetaremos los datos de una variable: *Ejemplo:*
python
edades=(10,20,30)
x,y,z=edades
print(x,y,z)
#10,20,30

Cómo podemos observar, cada datos de la variable edades se almacenaron en una letra y al imprimir ya no están dentro de una variable, y dejan de estar en una tupla ().

En caso de tener más variables podemos hacer lo siguiente: *Ejemplo:*
python
edades=(10,20,30,40,50)
x,_,_,_,z=edades
print(x,z)
#10,50
## "x" tomo el primer dato y "z" el último dato


## si imprimo (x,z,_) el guión bajo almacenará el último dato que está cerca a la `z` (el penultimo)

edades=(10,20,30,40,50)
x,_,_,_,z=edades
print(x,z,_)
#10,50,40


Otra manera sería usando *_, está tomará el valor de los datos que yo no le asigne una letra, en este caso el 20,30,40 y al imprimir no dara errores. **Ejemplo:**
python
edades=(10,20,30,40,50)
x,*_,z=edades
print(x,z)
#10,50

#si imprimo `*_` :
print(*_) #30,40,50



También podemos desempaquetar usando listas:
python
alturas=[1.76,1.68,1.87,1.65,1.90]
x,z,*_=alturas
print(x)
print(z)
print(*_)
# 1,76
# 1,90
# 1.68,1.87,1.65
```
### ARGUMENTOS POSICIONALES:
Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una tupla.
Pero python nos presenta algunas limitaciones si solo ponemos: suma(4,3,2,1), por ello usaremos el siguiente método:
```python
def _suma(*values):
    print(f'{values=}')
    resultado = 0
    for value in values:  # values es una tupla
        resultado += value
    return resultado


_suma(4, 3, 2, 1)
values=(4, 3, 2, 1)
#10


FUNCION PARA DESEMPAQUETAR:
python
values = (4, 3, 2, 1)
_suma(*values)
values=(4, 3, 2, 1)
#10


### ARGUMENTOS NOMINALES:

Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se empaqueten en un diccionario.

Supongamos un ejemplo en el que queremos encontrar la persona con mayor calificación de un examen. Haremos uso del ** para empaquetar los argumentos nominales:

python
def best_student(**marks):
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


best_student(ana=8, antonio=6, inma=9, javier=7)
marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
'inma'

Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ** en la llamada a la función para desempaquetar los argumentos nominales:

python
# Desempaquetado: best_student(ana=8, antonio=6, inma=9, javier=7)
best_student(**marks)
marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
'inma'
```
## Funciones internas de python (tarea)
## FUNCIONES INTERNAS 

1. La función `max` nos dice cuál es el “carácter más grande” de la cadena (que resulta ser la letra “u”), mientras que la función `min` nos muestra el carácter más pequeño (que en ese caso es un espacio).
```python
max('¡Hola, mundo!')
# 'u'
min('¡Hola, mundo!')
# ' '
```

2. `len` cuenta la cantidad de caracteres de un argumento.
```python
len('Hola, mundo')
#11
```
3. Función `isinstance()`, es una función complementaria de type
```python
# es como preguntar a python: ¿El valor es un string(otros valores)?, por lo que el programa responderá con True o False:
a="hola"
b=100
print(isinstance(a,string))
#True
```

4. La función `abs()`  devuelve el valor absoluto del número especificado.
```python
x = abs(3+5j)
```

5. La función `all()` devuelve Verdadero si todos los elementos de un iterable son verdaderos; de lo contrario, devuelve Falso. Si el objeto iterable está vacío, all() también devuelve Verdadero. No importa si son listas, tuplas, conjuntos, o diccionarios, si tiene 0, su resultado será False
```python
mylist = [0, 1, 1]
x = all(mylist)
```

6. La función `any()` devuelve Verdadero si algún elemento de un iterable es verdadero; de lo contrario, devuelve Falso. Si el objeto iterable está vacío, la any() función devolverá Falso.
```python
mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict) #True
# en los diccionarios está función verifica las claves, no lo valores.
```

1. La función `round()` devuelve un número de coma flotante, y lo redondea a entero.
```python
x = round(5.76543)
print(x) #6
```

1. La función reversed() devuelve un objeto iterador invertido.
```python
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x) #dcba
```

1. La función `zip()` devuelve un objeto zip, que es un iterador de tuplas donde el primer elemento de cada iterador pasado se empareja, y luego el segundo elemento de cada iterador pasado se empareja, etc. Si los iterables pasados tienen longitudes diferentes, el iterable con la menor cantidad de elementos decide la longitud del nuevo iterador.
```python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
# (('John', 'Jenny'), ('Charles', 'Christy')
```
10. La función `sorted()` devuelve una lista ordenada del objeto iterable especificado. Puede especificar orden ascendente o descendente. Las cadenas se ordenan alfabéticamente y los números se ordenan numéricamente.
```python
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

## Funciones internas de python (tarea)

- `int()` -> funcion que resive por parametro un texto y lo convierte a un entero
- `float`
## Tipos de Funciones
### Funciones anonimas (Funciones lambda)
una funcion que no tiene nombre
```python
lambda:"hola"
```

### Funciones closure
una funcion que dentro tiene una funcion
```python
def saludo(nombre):
    print(f"bienbenido{nombre}")
```

### Funciones callback
reciben por parametro otra funcion
```python
int(input("ingrese un numero: "))
```

### Programacion funcional
no requiere que yo sepa lo que el programa hace
```python
#programacion iterativa
lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
# programacion funcional
min(lista)

```

### tarea: averiguar y subir a GIT sobre map(), filter(), reduce()
# concepto y ejemplos

## TAREA: ENFOQUE FUNCIONAL
## map()
La función map() ejecuta una función específica para cada elemento en un iterable. El elemento se envía a la función como parámetro.
Esta función aplica otra función sobre cada elemento de un iterable. Supongamos que queremos aplicar la siguiente función: 
```python
def f(x):
    return x**2 / 2
data = range(1, 11)
map_gen = map(f, data)
type(map_gen)
map
list(map_gen)
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]
```
> [!NOTE]
Hay que tener en cuenta que map() devuelve un generador, no directamente una lista.

Podemos obtener el mismo resultado aplicando una función anónima «lambda»:
```python
list(map(lambda x: x**2 / 2, data))
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]
```
En Python es posible «simular» un map() a través de una lista por comprensión:
```python
[x**2 / 2 for x in data]
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]

# otro ejemplo:
# Calcule la longitud de cada palabra en la tupla:
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convertir el mapa en una lista, para facilitar la lectura:
print(list(x))
# <map object at 0x1493705c4130>
# [5, 6, 6]
```
## filter()
La funcion filter() devuelve un iterador donde los elementos se filtran a través de una función para probar si el elemento se acepta o no.
Esta función selecciona aquellos elementos de un iterable que cumplan una determinada condición. Supongamos que queremos seleccionar sólo aquellos números impares dentro de un rango:
```python
def odd_number(x):
    return x % 2 == 1
data = range(1, 21)
filter_gen = filter(odd_number, data)
type(filter_gen)
filter
list(filter_gen)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```
> [!NOTE]
Hay que tener en cuenta que filter() devuelve un generador, no directamente una lista.

Podemos obtener el mismo resultado aplicando una función anónima «lambda»:
```python
list(filter(lambda x: x % 2 == 1, data))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```
En Python es posible «simular» un filter() a través de una lista por comprensión:
```python
[x for x in data if x % 2 == 1]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# otro ejemplo:
# Filtre la matriz y devuelva una nueva matriz con solo los valores iguales o superiores a 18:
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)
# 18
# 24
# 32

```
## reduce()
Para poder usar esta función debemos usar el módulo functools. Nos permite aplicar una función dada sobre todos los elementos de un iterable de manera acumulativa. O dicho en otras palabras, nos permite reducir una función sobre un conjunto de valores. Supongamos que queremos realizar el producto de una serie de valores aplicando este enfoque:
```python
from functools import reduce
def mult_values(a, b):
    return a * b
data = range(1, 6)
reduce(mult_values, data)  # ((((1 * 2) * 3) * 4) * 5)
120
```
Aplicando una función anónima «lambda»…
```python
reduce(lambda x, y: x * y, data)
120
```
> [!NOTE]
Por cuestiones de legibilidad del código, se suelen preferir las listas por comprensión a funciones como map() o filter(), aunque cada problema tiene sus propias características y sus soluciones más adecuadas. Es un enfoque «más pitónico».
