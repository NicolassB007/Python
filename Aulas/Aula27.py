"""
Desenvolvendo um programa com POO, com o auxilio do professor
"""

class Bicicleta:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def honk(self):
        print("bibiiiii!!")

    def stop(self):
        print("Bicicleta parando...")
        print("Bicicleta parada!")

    def run(self):
        print("ACELERANDO...")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.honk()
b1.stop()
b1.run()