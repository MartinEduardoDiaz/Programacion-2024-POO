'''
Clases:
Gato, Area e Inventario

Gato
    Atributos:
        - Nombre
        - Edad
        - Nivel de energía
        - Nivel de hambre
    Estados:
        - Hambriento
        - Con energía
        - Cansado
    Acciones:
        - Jugar
        - Comer
        - Descansar

Area
    - Nombre
    - Capacidad máxima de gatos
    - Agregar un gato
    - Lista de gatos

Inventario:
    Metodos:
        - Describir
        - Agregar productos
        - Utilizar Productos
'''

class Gato():
    def __init__(self, nombre, edad, nivel_e, nivel_h):
        self.nombre = nombre
        self.edad = edad
        self.nivel_e = nivel_e
        self.nivel_h = nivel_h
    
    def alimentar():
        self.nivel_h - 20
    
    def jugar():
        self.nivel_h + 20
    
    def estado():
        if self.nivel_h < 40 and self.nivel_h >= 0:
            print(f"{self.nombre} está alimentado")
        elif self.nivel_h > 40 and self.nivel_h < 50:
            print(f"{self.nombre} no tiene hambre")
        elif self.nivel_h > 50 and self.nivel_h < 70:
            print(f"{self.name} tiene hambre")
        elif self.nivel_h > 70 and self.nivel_h <= 100:
            print(f"{self.name} tiene mucha hambre")

gato1 = Gato("Eva", 8, 40, 80)
gato2 = Gato("Nalu", 5, 80, 30)
gato3 = Gato("Pazuzu", 6, 50, 10)
gato4 = Gato("Coso", 2, 20, 80)
gato5 = Gato("Horus", 4, 30, 40)
gato6 = Gato("Fenrir", 3, 60, 80)
gato7 = Gato("Nerón", 5, 70, 70)
gato8 = Gato("Blanca", 7, 80, 30)
gato9 = Gato("Bigotes", 9, 40, 30)


###

class Area():
    def __init__(self, nombre, capacidad, lista):
        self.nombre = nombre
        self.capacidad = capacidad
        self.lista = {}

area1 = Area("sala_juegos", 10, {})
area2 = Area("sala_principal", 14, {})
area3 = Area("sala_exterior", 6, {})


###

class Inventario():
    def __init__(self, productos):
        self.productos = {}