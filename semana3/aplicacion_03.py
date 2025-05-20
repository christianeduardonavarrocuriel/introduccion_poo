# Ejemplo de parametros y tipos de datos
class Calculadora:

    def __init__(self):
        pass

    def sumar(self, numero1:int, numero2:int):
        resultado = numero1 + numero2
        print(f"Resultado: {resultado}")

    def dividir(self, divisor:float,dividendo:float):
        try:
            resultado = divisor / dividendo
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as error:
            print(f"Error 001 {error.args[0]}")
        except TypeError as error:
            print(f"Error 002 {error.args[0]}")
        except Exception as error:
            print(f"Error 003 {error.args[0]}")

    def restar (self, numero1: int, numero2: int)->int:
        resultado = numero1 - numero2
        return resultado
            
mi_calculadora = Calculadora()
mi_calculadora.sumar(10,5)
mi_calculadora.sumar("Hola ", "Adios")
mi_calculadora.dividir(10.0,0.0)
mi_calculadora.dividir("Hola",0.0)
        
print(f"Resultado: {mi_calculadora.restar(10,8)}")

resultado = mi_calculadora.restar(8,9)
print(f"Resultado: {resultado}")
