def operation_decorator(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            operation = None

        return func(first, second, operation)
    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return "Division by zero is undefined"
    elif operation == '*':
        return first * second


first_input = float(input("Enter the first number: "))
second_input = float(input("Enter the second number: "))

result = calc(first_input, second_input)
print(f"The result is: {result}")
