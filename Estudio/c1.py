
class Persona():
    # Bloque de Código
    
    # Atributos
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23

    # Métodos
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")

# Creación de un objeto de la clase Persona
persona1 = Persona()

# Accesoa os atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

# Llamando a los métodos de la clase
persona1.hablar()
persona1.caminar()