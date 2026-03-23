preço = float(input('Qual é o preço do produto? R$'))
novo_preço = preço - (preço * 5 / 100)

print('O produto que custava R${}, com 5% de desconto vai custar R${:.2f}'.format(preço, novo_preço))
