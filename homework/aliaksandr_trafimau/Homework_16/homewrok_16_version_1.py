import os
import dotenv
import mysql.connector as mysql
import csv

current_dir = os.path.dirname(__file__)
print(current_dir)

source_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data'))
source_file = os.path.join(source_dir, 'data.csv')
print(source_dir)
csv_set = set()
with open(source_file, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        csv_set.add(tuple(row.values()))
print(csv_set)

dotenv.load_dotenv()

db = mysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database=os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')
)

cursor = db.cursor()
cursor.execute("""
select DISTINCT students.name, students.second_name, groups.title, books.title, subjets.title, lessons.title,
marks.value
from students
left join books  on students.id  = books.taken_by_student_id
left join `groups`  on groups.id = students.group_id
left join marks  on marks.student_id = students.id
left join lessons  on lessons.id = marks.lesson_id
left join subjets on subjets.id = lessons.subject_id
""")

columns = [col[0] for col in cursor.description]
db_data = cursor.fetchall()
db_set = set(tuple(row) for row in db_data)

differences = csv_set.difference(db_set)
print('Missing data')
for differince in differences:
    print(differince)
db.commit()

cursor.close()
db.close()
