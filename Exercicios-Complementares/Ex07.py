valor = input("Primeiro valor: ")
valor2 = input("Segundo valor: ")

valor_para_int = int(valor)
valor2_para_int = int(valor2)

checagem_primeiro_valor_maior = valor_para_int > valor2_para_int
checagem_segundo_valor_maior = valor2_para_int > valor_para_int

print(f"{valor} é maior que {valor2}? {checagem_primeiro_valor_maior}")
print(f"{valor2} é maior que {valor}? {checagem_segundo_valor_maior}")