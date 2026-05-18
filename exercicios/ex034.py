salario = float(input("Digite o salário do funcionário: R$"))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"O valor do aumento será de: R${aumento:.2f}")
print(f"O novo salário será de: R${salario + aumento:.2f}")
