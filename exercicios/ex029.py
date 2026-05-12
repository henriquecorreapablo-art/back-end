velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido de 80km/h.")
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"O valor da multa é de R${multa:.2f}")
print("Dirija com segurança!")
