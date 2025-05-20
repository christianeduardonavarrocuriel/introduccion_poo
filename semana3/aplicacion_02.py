class Calculadora:

    #Metodo inicial o constructor de la clase
    def __init__(self):
        #Indica que se ejecuto correctamente yu que pase a la siguiente instrucción
        pass

    #Metodo sumar que recibe 2 parametros: numero1 y numero2
    def sumar(Self, numero1, numero2):
        #Variable que almacena la suma 
        resultado=numero1+numero2
        #Imprime en consola el texto Resultado y el valor del resultado
        print(f"Resultado: {resultado}")

    #Metodo restar que recibe 2 parametros: numero1 y numero2
    def restar(self, numero1,numero2):
        #Indica que el metodo se genero correctamente y esta listo para implementar el codigo necesario
        pass

#Se crea una instancia de la clase Calculadora, es decir se crea un objeto
mi_calculadora = Calculadora()
#Invoca el metodo sumar del objeto
mi_calculadora.sumar(10,5)