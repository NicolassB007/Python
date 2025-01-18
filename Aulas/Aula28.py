# Construtores e Destrutores

class Cachorro:
    def __init__(self, name, color, awake=True):
        print("Inicializando a classe")
        self.name = name
        self.color = color
        self.awake = awake
    
    def __del__(self):
        print("Removendo a instância da classe")

    def honk(self):
        print("ruf ruf")
    
def create_dog():
    dog = Cachorro("Alado", "Preto", False)    
    print(dog.name)
    
# dog = Cachorro("Rex", "Cinza")
# dog.honk()
create_dog()