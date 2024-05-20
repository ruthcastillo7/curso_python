# controles de flujo
Creando `bifurcaciones` o creando `repeticion` de instrucciones.

todos los programas trabajan a travez de instrucciones ordenadas.
existen maneras de romper con el flujo normal de los programas creando
`bifurcaciones` o creando
`repeticiones` de instrucciones.
## decisiones
### la sentencia if
la sentencia de decicicon en python es `if`, en su escritura debemos añadiruna **exprecion de comparacion**
terminando con `:` al final de la linea
> ejemplo:

```python
if True:
    print("es verdad")
```
## ciclos
son los controles de flujo que repiten codigo y si sintaxis es la siguiente:
### FOR
este 
>para FOR:
```python
#este codigon imprime los numeros
#del 1 al 10
for n in range(1,11).
print(n)
```
```python
#primer ejemplo if esctructurado
edad: int=(input("escribe tu edad: "))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
#segundo ejemplo if alamcenado en variable
edad_dos:int=int(input("escribe tu edad: "))
respuesta: str="eres mayor" if edad_dos>18 else "eres menor"
print(respuesta)
```

clase de hoy 15/05/24
1. `enumerate` consume mas memoria pero en oraciones largas es mas veloz que el range, pero si son cortos es mas lento
oraciones largas: funciona mejor
medianas: funciona mejor
```python
for i,l in enumerate("aeiou"):
```
2. `range` su comsumo de memoria en este caso es menos y mas veloz siempre y cuando sea una oracion corta
oraciones pequeñas: es mas rapido
```python
for n in range(0,len(oracion)):
```

clase de hoy 20/05/24
## while
es un mecanismo que usa `python` para repetir instrucciones, la sematica de esta sentencia es : `mientras se cumpla la funcion has algo`
```python
while (): #si lo que esta en parentecis es verdad entonces print
#si es falso no entra a la ejecucion y cierra el programa
   print
```

en `FOR` sabemos cuando termina, ya que tebnemos sus indices (se usa para recorrer textos o listas)
en `WHILE` se usa cuando el ciclo necesita la intervencion de un  tercero para que termine la ejeccucion