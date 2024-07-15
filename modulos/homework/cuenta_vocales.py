"""modulo de vocales de edad"""
def f_cuenta_vocales(text:str):
    """funcion para contar de vocales a que aparecer en un texto"""  # el dog string es importtante para saber que hacer al ejecutar 
    text_minusculas:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales