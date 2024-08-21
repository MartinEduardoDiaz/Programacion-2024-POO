
class Persona():
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
        # Métodos
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")