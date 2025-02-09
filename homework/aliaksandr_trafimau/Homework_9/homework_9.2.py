import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

def hot_temperature(x):
    return x > 28

list_hot_temperatures = list(filter(hot_temperature, temperatures))

print(list_hot_temperatures)
print(max(list_hot_temperatures))
print(statistics.median(list_hot_temperatures))
