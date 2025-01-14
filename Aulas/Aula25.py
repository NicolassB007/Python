# Funções

# Primeira função
# def boas_vindas():
#     print("Hello World!")

# def exibir_mensagem(nome):
#     print(f"Seja bem-vindo {nome}")

# def exibir_mensagem2(nome="Anônimo"):
#     print(f"Seja bem-vindo {nome}")

# boas_vindas()
# exibir_mensagem("Nicolas")
# exibir_mensagem2()

# # Funções podem retornar um valor ou mais de um

# def soma_numeros(numeros):
#     return sum(numeros)

# print(soma_numeros([1, 4, 5, 5]))


# Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    # Salvar carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Tres formas de inserir os valores
# salvar_carro("Fiat", "Palio", 1999, "ABC-1231")
# salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1231") # Uma b
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1231"})


# *args e **kwargs
# *args recebe os valores em uma tupla
# **kwargs recebe os valores em um dicionário