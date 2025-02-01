a = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = a.replace(',', '').replace('.', '').split()
b = [word + 'ing' for word in words]
c = ' '.join(b)
print(c)
