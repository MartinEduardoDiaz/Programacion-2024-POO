# Constructor
class Persona():
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)

    def calcular_imc(self):
        imc = self.peso / self.altura**2
        print(f"El IMC de la persona es: {imc}")
        

# Persona
persona1 = Persona(nombre="Martin", apellido="Diaz", edad="18", altura=1.65, peso=68)

# Método calcular_imc() en persona1
persona1.calcular_imc()
