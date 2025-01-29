my_dict = {
    'tuple': (133, True, 'TA_1', 'TA_2', 666),
    'list': [0.223, False, 'AT_1', 'AT_2', 999],
    'dict': {
        'A': '1',
        'B': 'AT_1222',
        'C': False,
        'D': '0',
        'E': ''
    },
    'set': {0.0004, None, '1_AT', '2_AT', 0.23456}
}

print(my_dict['tuple'][-1])

my_dict['list'].append("new_element")
del my_dict['list'][1]
print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = "0.0004"
del my_dict['dict']['B']
print(my_dict['dict'])

my_dict['set'].add('ADS')
my_dict['set'].discard('1_AT')
print(my_dict['set'])
