# Estrutura Condicional
# if(se) -> Condicional simples -> Unico desvio
# if/else (se/senao) -> Condicional com dois desvios
# if/elif/else -> Para ter mais desvios

# MAIOR_IDADE = 18
# idade = input("Informe sua idade: ")
# idade_convertido_para_int = int(idade)

# # Usando if
# if idade_convertido_para_int >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar sua CNH!")

# if idade_convertido_para_int < MAIOR_IDADE:
#     print("Você é menor de idade, não será possível fazer a sua CNH")


# Usando if/else
# MAIOR_IDADE = 18
# idade = input("Informe sua idade: ")
# idade_convertido_para_int = int(idade)

# if idade_convertido_para_int >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar sua CNH!")

# else:
#     print("Você é menor de idade, não será possível fazer a sua CNH")

# Usando if/elif/else
# MAIOR_IDADE = 18
# IDADE_ESPECIAL = 17
# idade = input("Informe sua idade: ")
# idade_convertido_para_int = int(idade)

# if idade_convertido_para_int >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar sua CNH!")

# elif idade_convertido_para_int == IDADE_ESPECIAL:
#     print("Você pode fazer apenas as aulas teóricas! ")

# else:
#     print("Não pode tirar sua CNH")


# Estrutura condicional aninhada
# conta_normal = False
# conta_universitaria = False
# saldo = 200
# saque = 500.0
# cheque_especial = 450.0

# if conta_normal:
#     if saldo >= saque:
#         print("Saque efetuado com sucesso!")
#     elif saque <= (saldo + cheque_especial):
#         print("Saque realizado com cheque especial")
#     else:
#         print("Não foi possível realizar o saque!")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realizado com sucesso!")
#     else:
#         print("Saldo insuficiente")
# else:
#     print("Sistema não reconheceu seu tipo de conta! Entre em contato com o Gerente")


# Operador ternário
saldo = 760
saque = 761
saldo_final = saldo - saque
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
print(f"Saldo final {saldo_final}")