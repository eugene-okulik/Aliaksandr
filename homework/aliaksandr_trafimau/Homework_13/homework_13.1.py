import datetime
import os

current_dir = os.path.dirname(__file__)
print(current_dir)

source_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'eugene_okulik', 'hw_13'))
source_file = os.path.join(source_dir, 'data.txt')
print(source_dir)

def process_dates():
    with open(source_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split(' - ')
        date_str = parts[0].split('. ')[1]
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if "на неделю позже" in parts[1]:
            new_date = date + datetime.timedelta(weeks=1)
            print(f"Дата на одну неделю после указанной: {new_date}")
        elif "какой это будет день недели" in parts[1]:

            day_of_week = date.strftime('%A')
            print(f"День недели: {day_of_week}")

        elif "сколько дней назад была эта дата" in parts[1]:
            now = datetime.datetime.now()
            delta = now - date
            print(f"Количество дней назад: {delta.days} дней")


process_dates()
