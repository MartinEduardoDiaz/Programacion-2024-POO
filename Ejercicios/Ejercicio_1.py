
class Persona():
    # Bloque de Código
    
    # Atributos
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23
    altura = 1.70
    peso = 65.8

    # Métodos
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def calcular_imc(self):
        

# Creación de un objeto de la clase Persona
persona1 = Persona()

# Accesoa os atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
print(f"Altura: {persona1.altura} metros")
print(f"Peso: {persona1.peso} Kg")

# Llamando a los métodos de la clase
persona1.hablar()
persona1.caminar()