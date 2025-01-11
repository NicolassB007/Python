# Estrutura de repetição
# Comando for
# For é usado para percorrer um objeto iterável.
# É recomendado utiliza-lo quando se sabe previamente quantas repetições serão

# palavra = input("Informe uma palavra: ")
# VOGAIS = "aeiou"

# for letra in palavra:
#     if letra in VOGAIS:
#         print(letra)


# for letra in "Python":
#     print(letra)

# Utilizando for com range
# Range ->    (start, stop(stop - 1), step)
# range(20)-  (0, 19, 1)
# range(0,15)-(0, 14, 1)
# range(0,51, 5) - (0, 50, 5) 

# for i in range(10):
#     print(i)

# for i in range(0, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# Utilizando o WHILE
# Utilizamos ele para repetir um bloco de códigos, como no for
# PORÉM, utilizamos o while quando não sabemos quantas repetições serão
# Ex.: O código pode executar, 2 vezes, 4 vezes, 19, vezes, 1 vez

# opcao = -1

# while opcao != 0:
#     opcao = int(input("[ 1 ] -> Sacar \n[ 2 ] -> Extrato \n[ 0 ] -> Sair \n"))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo o extrato...")


# Utilizando o break e o continue

while True:
    numero = int(input("Um valor: "))

    if numero == 5:
        break

    if numero == 2:
        continue

    if numero == 11:
        continue

    print(numero)
