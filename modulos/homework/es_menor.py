"""modulo de funcion menor de edad"""
def f_es_menor(lista:list): #aqui debemos especificar, poner (lista:list), si no hacemos esto nos aparece el errer de amy
    """funcion para saber el numero menor de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
    return menor