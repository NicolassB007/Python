# Estrutura de Dado - Dicionário

# Criando um dicionário
pessoa = {"nome": "Nicolas", "idade": 17}
print(pessoa["nome"])

# Usando o construtor do dicionário
pessoa2 = dict(nome="Leticia", idade=21)
print(pessoa2)

# Colocando mais um valor no dicionário
pessoa["telefone"] = "3123-1231" 
print(pessoa)

# É possível fazer dicionários aninhados
contatos = {
    "novocliente@gmail.com": {"nome":"Clara", "numero": "1231-2314"},
    "helianeempresa@gmail.com": {"nome": "Heliane", "numero": "3331-2224"},
    "claudiohenrique@gmail.com": {"nome": "Claudio", "numero": "1521-1112"}
}

telefone = contatos["helianeempresa@gmail.com"]["numero"]
print(telefone)

# É possível iterar um dicionário
for chave in contatos:
    print(chave, contatos[chave])