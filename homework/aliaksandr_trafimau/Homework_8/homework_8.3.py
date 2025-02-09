import random

salary = int(input("Enter a number: "))
random_bonus = random.randint(100, 5000)
bonus_bool = random.choice([True, False])

if bonus_bool:
    total_salary = salary + random_bonus
    print(salary, bonus_bool, '$', total_salary)
else:
    print(salary, bonus_bool, '$', salary)
