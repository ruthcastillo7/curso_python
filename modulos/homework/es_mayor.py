"""modulo de funcion mayor de edad"""
def f_es_mayor(lista:list):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor #identacion: el return debe estar dentro de la funciopn o sea e def no en for o if