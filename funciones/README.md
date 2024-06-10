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