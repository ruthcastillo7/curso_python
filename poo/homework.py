# EJERCICIO 1
# Crear una clase Banco
# sus atributos seran nombre, apllidos, dni, numero de cuenta y saldo inicial
# como metodos podemos hacer deposito retirar dinero y ver estado de cuenta

class Banco:
    def __init__(self,nombre,apellido,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial
        # metodos
    def deposita(self,monto):
        print("esta depositando: S/. ", monto)
    def retirar(self,monto):
        print("esta retirando: S/. ",monto)
    def ver(self):
        print("ve su estado de cuenta")

ruth=Banco("ruth","castillo",60414454,2324-2342-3334,100)
ruth.deposita(200)
ruth.retirar(90)
ruth.ver()

# EJERCICIO 2
# Crear una clase agencia
# con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje
