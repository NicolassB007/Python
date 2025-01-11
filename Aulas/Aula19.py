# Estrutura de dado - Lista

# frutas = ["Maçã", "Uva", "Manga"]
# print(frutas)

# # Posso declarar uma lista vazia
# frutas2 = []
# print(frutas2)

# letras = list("Python")
# print(letras)

# numeros = list(range(10))
# print(numeros)

# # Lista suporta muitos valores e de mais de um tipo
# carro = ["Honda", "Civic", 120000, 1000, True]
# print(carro)

# # Posso acessar conteúdos da lista através dos indices
# print(carro[2])

# # Percorrendo uma lista com o for
# lista2 = ["Unesp", "ETEC", "UFSCAR"]
# for itens in lista2:
#     print(itens)


# for indice, item in enumerate(carro):
#     print(f"{indice}: {item}")


# List Comprehension
# pares = []

# for par in lista:
#     if par % 2 == 0:
#         pares.append(par)
# print(pares)

lista = [1, 4, 10, 32, 33, 43, 13, 9]
pares = [par for par in lista if par % 2 == 0]
print(pares)