# Estrutura de Dados - Conjuto

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("Abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

# Não é possível acessar os valores de um conjunto, para isso é necessário converte-lo para lista para podermos acessar um indice

numeros = list(numeros)
print(numeros[1])

# Métodos da Estrutura de Dados - Set
# .union() -> Uni dois conjuntos, como na matemática
# .intersection() -> Pega a interseção, como na matemática
# .difference() -> Mostra o item que tem em um conjunto e não tem no outro
# .symetric_difference
# .issubset() -> Mostra se um conjunto está dentro de outro
# .isupperset()
# .isdisjoint()
# .add() -> É possível adicionar valores no set caso o valor informado não esteja no conjunto
# .clear() 
# .copy()
# .discard() -> Descarta um valor informado no set
# .pop() -> Remove o primeiro valor, caso seja utilizado no set
# .remove() -> Remove o valor no indice informado, caso não exista o indice ele volta um erro
# .len() -> Mostra o tamanho do set