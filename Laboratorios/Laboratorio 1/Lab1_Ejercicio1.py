class Personaje():
    def __init__(self, nombre, vida, ataque):
        self.nombre = str(nombre)
        self.vida = int(vida)
        self.ataque = int(ataque)
    

    def estadisticas(self):
        print(f"El personaje se llama {self.nombre}")
        print(f"El personaje tiene {self.vida} puntos de vida")
        print(f"El personaje tiene {self.ataque} puntos de ataque")
    
    def atacar(self):
        print(f"{self.nombre} ha atacado")
    
    def recibir_daño(self):
        print(f"{self.nombre} a recibido daño")
        print(f"{self.nombre} tiene {self.vida - 50} puntos de vida")


personaje1 = Personaje("M", 1000, 50)
personaje2 = Personaje("S", 2000, 100)

print(personaje1.estadisticas())
print(personaje2.estadisticas())

print(personaje1.atacar())
print(personaje2.recibir_daño())