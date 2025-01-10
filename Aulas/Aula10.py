# Operadores lógicos

# Tabela verdade 'and'
print(True and True) # True
print(True and False) # False 
print(False and True) # False 
print(False and False) # False 

print('\n')

# Tabela verdade 'or'
print(True or True) # True
print(True or False) # True 
print(False or True) # True 
print(False or False) # False 

saldo = 1000
saque = 250
limite_saque = 200
conta_especial = True

print('\n')

expressao = saldo >= saque and saque <= limite_saque or conta_especial and saldo >= saque
print(expressao)

# Forma mais legivel e com boas práticas
expressao_2 = (saldo >= saque and saque <= limite_saque) or (conta_especial and saldo >= saque)
print(expressao_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite_saque)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

checando = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente