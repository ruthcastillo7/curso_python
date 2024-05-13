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