numero = int(input("Digite um número inteiro qualquer: "))
print("\nEscolha a base de conversão:")
print("[ 1 ] para BINÁRIO")
print("[ 2 ] para OCTAL")
print("[ 3 ] para HEXADECIMAL")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"O número {numero} convertido para BINÁRIO é igual a: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O número {numero} convertido para OCTAL é igual a: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O número {numero} convertido para HEXADECIMAL é igual a: {hex(numero)[2:]}")
else:
    print("Opção inválida! Tente novamente escolhendo 1, 2 ou 3.")
