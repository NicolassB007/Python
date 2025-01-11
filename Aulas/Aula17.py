# Fatiamento de String

nome = "Nicolas Bissotto da Silva"
# Podemos acessar nossa string através dos indices
# Ex.: nome[start:stop:step]
# Ex.: nome[0] -> 'N'

print(nome[0])
print(nome[3])

print(nome[:6]) # Da primeira letra até a 5 letra
print(nome[:7]) # Da primeira letra até a 6 letra

print(nome[::2]) # Da primeira letra até a ultima pulando de 2 em 2 
# (duas letras em duas letras)

print(nome[::-1]) 

print(nome[-3]) # Pegando a ultima letra do meu nome