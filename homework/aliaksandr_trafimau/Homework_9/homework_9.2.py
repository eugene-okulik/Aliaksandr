import statistics

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


def is_hot_temperature(x):
    return x > 28


hot_temperatures = list(filter(is_hot_temperature, temperatures))

print("Горячие температуры:", hot_temperatures)
print("Максимальная температура:", max(hot_temperatures))
print("Медиана горячих температур:", statistics.median(hot_temperatures))
