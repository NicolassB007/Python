# Métodods uteis para String

nome = "NiColAs"

# Deixando a string maiuscula
print(nome.upper(),'\n')

# Deixando a string minuscula
print(nome.lower(), '\n')

# Deixando apenas a primeira letra maiuscula
print(nome.title(), '\n')

# Eliminando espaços em branco
string2 = '   Curso de Python   ' # String com espaços em branco
print(string2)

# Removendo espaços
print(string2.strip(), end='#\n')

# Removendo espaços da esquerda
print(string2.lstrip(), end='#\n')

# Removendo espaços da direita
print(string2.rstrip(), end='#\n')

# Centralizando

menu = "Python"
print(menu.center(15, "-"))

# Colocando algum caracter entre as letras
print('.'.join(menu))