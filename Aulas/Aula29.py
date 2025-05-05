# Herança simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Nao"} estou carregado")


# moto = Motocicleta("Branca", "aasb-121", 2)
# moto.ligar_motor()

# carro = Carro("Preto", "aqpo-112", 4)
# carro.ligar_motor()

caminhao = Caminhao("Cinza", "asca-1231", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()