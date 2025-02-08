def fib_inf():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
gen_fib_inf =fib_inf()

numbers = {5, 200, 1000, 10000}
results = {}
current_position = 1

for fib_number in gen_fib_inf:
    if current_position in numbers:
        results[current_position] = fib_number
        if len(results) == len(numbers):
            break
    current_position += 1

for position in sorted(results):
    print(f"{position} - {results[position]}")
