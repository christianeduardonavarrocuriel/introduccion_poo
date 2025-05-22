"""
Ejemplo de uso de cadenas
"""

class Cadenas:
    #Variables de clase
    nombre = None
    password = None

    def __init__(self, texto:str)->None:
        self.texto = texto
        self.variable_local= "John Cena"

    def longitud(self) -> None:
        print(len(self.texto))
        print(self.variable_local)
        self.otra_variable = 9
        print(self.nombre)        

    def caracter(self, posicion:int) -> None:
        print(self.texto[posicion])

    def alcanceVariables (self, variable_local:str) -> None:
        print(self.texto)
        print(variable_local)
        print(self.variable_local)

mi_objeto = Cadenas("Hola")
mi_objeto.longitud()
mi_objeto.caracter(2)

mi_objeto.alcanceVariables("adios")