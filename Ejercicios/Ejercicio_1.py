'''
Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
Propiedades a la clase Persona:

altura (float): Representa la altura de la persona en metros.
peso (float): Representa el peso de la persona en kilogramos.

Modificar el constructor __init__ para aceptar estos nuevos parámetros y asignarlos a las propiedades
correspondientes.

- Agregar un nuevo método para calcular el IMC
    - El método calcular_imc() debe calcular el Índice de Masa Corporal (IMC) de la persona utilizando la
      fórmula (peso/altura^2)
    - El método debe devolver el valor del IMC y mostrar un mensaje indicando si la persona está en un
      rango de peso normal, bajo peso, sobrepeso, u obesidad basado en el valor calculado.

- Agregar un método llamado promedio_asignatura() a la clase Persona().
    - Este método debe recibir tres notas (valores de tipo float) como parámetros.
    - El método debe calcular el promedio de estas tres notas.
    - Si el promedio es igual o superior a 4.0, el método debe imprimir un mensaje indicando que la
      persona aprobó la asignatura; de lo contrario, debe indicar que la persona no aprobó.
'''

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