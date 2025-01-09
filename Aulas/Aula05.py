# Convertendo tipos

# Convertendo float para int
numero = 5.2
print(f"Antes da conversão {numero}")
numero_convertido_para_int = int(5.2) 
# Converter float para int pode ser ruim, pois, pode causar perda
# de informação!
print(f"Depois da conversão {numero_convertido_para_int}")

# Convertendo String para int
numero2 = '2'
numero2_convertido_para_int = int(numero2)
print(numero2_convertido_para_int)

# Convertendo int para float
numero3 = 5
numero3_para_float = float(numero3)
print(numero3_para_float)

# Convertendo string para float
numero4 = '1.5'
numero4_para_float = float(numero4)
print(numero4_para_float)

# Float para String
numero5 = 1.7
numero5_para_string = str(numero5)

# Vendo qual é o tipo da variavel
print(type(numero_convertido_para_int))
print(type(numero2_convertido_para_int))
print(type(numero3_para_float))
print(type(numero5_para_string))