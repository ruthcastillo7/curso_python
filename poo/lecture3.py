# crear una classe de alumnos con los atributos que ud. crea por conveniente
# luego instanciara a 4 alumnos
# class Alumno: # siempre singular
#     def __init__(self,nombre,apellido,edad,dni):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.edad=edad
#         self.dni=dni

# rosa=Alumno("rosa","flores",12,60424456)
# print(rosa.nombre)
# romulo=Alumno("romulo","quispe",18,80424456)
# print(romulo.apellido)
# mire=Alumno("mire","ramires",15,77424456)
# claudia=Alumno("claudia","ramos",13,60424460)

#metodo del profe
class Alumno: # siempre singular
    def __init__(self,nombre,edad,gmail,programa_estudio="APSTI"): # aqui asigno un valor por defecto
        self.nombre=nombre
        self.edad=edad
        self.gmail=gmail
        self.programa_estudio=programa_estudio
    #metodos
    def escribir(self):
        print("estoy escribiendo")
    def tarea(self,nombre_docente):
        print("haciendo la tarea de:",nombre_docente)
    def terminar_tarea(self):
        print("terminando tarea anterios")

maricielo=Alumno("maricielo",18,"yo@gmail")
print(maricielo.programa_estudio)
mercedes=Alumno("mercedes",15,"tu@gmail.com","enfermeria")
print(mercedes.programa_estudio)

maricielo.tarea("Alicia")
maricielo.terminar_tarea()
maricielo.tarea("Alvarez")