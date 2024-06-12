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


### Desempaquetado/Empaquetado de argumentos (tarea)
## Funciones internas de python (tarea)