## 1. crear una funcion que resiva N numeros
# por argumrntos y retorne una list acon los numeros pares
# def num_pares(*args):
#     lista_pares=[]
#     for n in args:
#         if n%2==0:
#             lista_pares.append(n)
#     return lista_pares
# #por comprencion
# #return [n for n in args if n%2==0]
# print(num_pares(8,5,4,7,9,25,4,7,12)) #[8, 4, 4, 12]

# 2. crear 3 funciones para los siguentes casos
# calcular en numero menor 
# calcular el numero mayor
# y calcular la suma de todos los numeros
#observacion: se le pasara por aurgumnento N numeros
def Min(*args):
    menor=args[0]
    for n in args:
        if n>menor:
             menor=n
    return menor
def Max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
             mayor=n
    return mayor
def Sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma
valores=4,7,8,5,2,1
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))