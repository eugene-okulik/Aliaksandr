import datetime

my_time = "Jan 15, 2023 - 12:05:33"

python_format = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")
human_format = python_format.strftime('Year: %Y, month: %B, day: %d')
full_month = python_format.strftime('%B')
formatted_date = python_format.strftime('%d.%m.%Y, %H:%M')

print(python_format)
print(human_format)
print(full_month)
print(formatted_date)
