numero = input("Informe um valor: ")
numero_para_int = int(numero)

par_impar = numero_para_int % 2 == 0

print(f"O numero {numero} é PAR? {par_impar}")