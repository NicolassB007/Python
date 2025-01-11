valor = input("Primeiro valor: ")
valor2 = input("Segundo valor: ")

valor_convertido_para_int = int(valor)
valor2_convertido_para_int = int(valor2)

soma = valor_convertido_para_int + valor2_convertido_para_int
subt = valor_convertido_para_int - valor2_convertido_para_int
multi = valor_convertido_para_int * valor2_convertido_para_int
divisao = valor_convertido_para_int / valor2_convertido_para_int

print(f"SOMA = {soma}")
print(f"SUBTRAÇÃO = {subt}")
print(f"MULTIPLICAÇÃO = {multi}")
print(f"DIVISÃO = {divisao}")