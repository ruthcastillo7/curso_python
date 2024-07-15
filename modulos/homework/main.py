"""# este es el script principal"""
import mayor_edad
import es_mayor
import es_menor
import cuenta_vocales
mayor_edad.funcion_mayor_edad(20)
print(es_mayor.f_es_mayor([7,4,2,1,0,8]))
print(es_menor.f_es_menor([7,4,5,2,3,0]))
print(cuenta_vocales.f_cuenta_vocales("gola casyynh lrroek")) #aqui buscara "a" por que en el modulo cuenta_vocales "if n == "a":""

## otra manera
## from mayor_edad import funcion_mayor_edad  (para importar)  (en lugar de la linea 2)
## funcion_mayor_edad(20)  (en lugar de la linea 6)

# mayor_edad(20)  #aqui simplemnete ponemos asi sin "print" porque anteriormente ya posimos print (linea 5 y 7)
# es_menor([4,8,10,2,3,0]) para hacer esto debemos usar el print
#print(es_menor([4,8,10,2,3]))
#print(cuenta_vocales("mi mama me mima yo amo a mi mama"))
