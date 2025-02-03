a = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero.'
)

words = a.split()
b = []

for word in words:
    if word[-1] in ',.':
        b.append(word[:-1] + 'ing' + word[-1])
    else:
        b.append(word + 'ing')

c = ' '.join(b)
print(c)
