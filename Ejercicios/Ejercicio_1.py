
class Persona():
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
        # Métodos
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")
    
    def calcular_imc(self):
        imc = peso/altura**2