number = list(range(1, 101))
for at in number:
    if at % 3 == 0 and at % 5 == 0:
        print('FuzzBuzz')
    elif at  % 3 == 0:
        print('Fuzz')
    elif at % 5 == 0:
        print('Buzz')
    else:
        print(at)
