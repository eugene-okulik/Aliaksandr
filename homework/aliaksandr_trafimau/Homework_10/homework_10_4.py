price_list = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in price_list.split('\n')}
print(price_dict)
