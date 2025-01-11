# Formatação de strings -> f-strings

# Interpolando com %

# nome = "Nicolas"
# idade = 17
# hobby = "Programação"
# linguagem = "Python"

# print("Meu nome é %s, tenho %d, estou estudando %s e estou fazendo um curso de %s" % (nome, idade, hobby, linguagem))

# Interpolando com format

nome = "Nicolas"
idade = 17
hobby = "Programação"
linguagem = "Python"

print("Meu nome é {}, tenho {}, estou estudando {} e estou fazendo um curso de {}".format(nome, idade, hobby, linguagem))

# Podemos usar o format junto com o indice
print("Meu nome é {1}, tenho {3}, estou estudando {0} e estou fazendo um curso de {2}".format(hobby, nome, linguagem, idade))

# Temos a f-string
print(f"Meu nome é {nome}, tenho {idade}, estou estudando {hobby} e estou fazendo um curso de {linguagem}")

# Formatando valores
PI = 3.14159
print(f"{PI:.2f}")
print(f"{PI:8.2f}")
print(f"O valor de PI é {PI:.2f}")