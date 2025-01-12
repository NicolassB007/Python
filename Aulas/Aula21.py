# Tuplas

# Declarando uma tuplas
tupla = ("Nicolas", "Marcos", "Ronaldo" ,"Pedro",)
print(tupla)

# Acessando dados da Tuplas
print(tupla[2])

# Fatiamento
tupla2 = ('P', 'y', 't', 'h', 'o', 'n')
print(tupla2[:4])
print(tupla2[::])
print(tupla2[2:6:])
print(tupla2[::-1])

# Iterando minha Tuplas
for item in tupla:
    print(item)

# Métodos que pode ser usado na Tupla
# count() - Contar quantas vezes determinado valor aparece
# index() -> Mostra qual é o indice do valor informado nos parenteses
# len