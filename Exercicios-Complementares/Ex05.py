ano = input("Ano: ")
ano_para_int = int(ano)

divisivel_por_4 = ano_para_int % 4 == 0

ano_bissexto = divisivel_por_4
print(f"O ANO {ano} é BISSEXTO? {ano_bissexto}")