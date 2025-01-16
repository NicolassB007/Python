# Continuação da aula anterior sobre Funções
# Parâmetros especiais
# É possível "forçar" qual será o tipo de parâmetro, como apenas parâmetro posicional, ou posicional e nomeado...

# Ex.:
# Apenas Argumentos posicionais       # Apenas agumentos nomeados!
# def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

#             # Argumentos posicionais     # Argumentos nomeados!
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina",) # VÁLIDO

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # INVÁLIDO



# Outro Exemplo
# def criar_carro(modelo, ano, placa, /,  marca,  *, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina",) # VÁLIDO

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # INVÁLIDO



# É POSSÍVEL UTILIZAR UMA FUNÇÃO COMO PARÂMETRO DE OUTRA
# def soma(a, b):
#     return a + b

# def exibir_resultado(a, b, funcao):
#     resultado = funcao(a, b)
#     print(f"O resultado da operação {a} + {b} = {resultado}")

# exibir_resultado(2, 5, soma)

# Variáveis global
salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(230))