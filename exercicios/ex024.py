cidade = str(input('Em que cidade você nasceu? ')).strip()
comeca_com_santo = cidade[:5].upper() == 'SANTO'
print(f'A cidade começa com "Santo"? {comeca_com_santo}')
