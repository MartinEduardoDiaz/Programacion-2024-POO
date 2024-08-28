class Persona():
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)
    
    def hablar(self):
        print(self.nombre, "está hablando")
    
    def caminar(self):
        print(f"{self.nombre} está caminando")
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando")
    
    def saber_imc(self):
        imc = self.peso / (self.altura * self.altura)
        print("El imc de", self.nombre, "es:", imc)


persona1 = Persona("Cristina", "Torres", 20, 1.6, 65)

print(persona1.caminar())
print(persona1.hablar())
print(persona1.estudiar())
print(persona1.saber_imc())