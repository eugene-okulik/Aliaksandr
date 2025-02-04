def extract(text_list):
    total_sum = 0
    for text in text_list:
        number = int(text.split(":")[-1].strip())
        result = number + 10
        total_sum += result
    print("Sum:", total_sum)


extract([
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
])