class Persona():

    # Atributos
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23

    # Metodos
    def hablar(self):
        print(f"{self.nombre} está hablando")
    
    def caminar(self):
        print(f"{self.nombre} está caminando")
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")


# Creación de un objeto de la clase Persona
persona1 = Persona()

# Acceso a los atributos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad}")

# Llamando a los métodos de la clase
persona1.hablar()
persona1.caminar()
persona1.estudiar()
persona1.dormir()