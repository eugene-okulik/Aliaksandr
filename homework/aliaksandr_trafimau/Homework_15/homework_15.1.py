import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Aliaksandr2', 'Trafimau2',)
cursor.execute(query, values)
student_id = cursor.lastrowid
print(f"{student_id}")

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES  (%s, %s, %s)"
values = ('AT_Group_2', '2023-08-01', '2040-09-30')
cursor.execute(query, values)
group_id = cursor.lastrowid
print(f"{group_id}")

update_query = "UPDATE students SET group_id = %s WHERE id = %s"
update_value = (group_id, student_id)
cursor.execute(update_query, update_value)

query = 'insert into books (title, taken_by_student_id) values (%s, %s) '
values = [
    ('Echoes of Time1', student_id),
    ('Beyond the Horizon1', student_id),
    ('The Last Symphony1', student_id)
]
cursor.executemany(query, values)

query = 'insert into subjets (title) values (%s) '
values = [
    ('AT_Sub_11',),
    ('AT_Sub_22',),
    ('AT_Sub_33',)
]

sub_ids = []

for value in values:
    cursor.execute(query, value)
    subjets_id = cursor.lastrowid
    sub_ids.append(subjets_id)
subject_id_1 = sub_ids[0]
subject_id_2 = sub_ids[1]
subject_id_3 = sub_ids[2]

query = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
values = [
    ('lesson_11', subject_id_1),
    ('lesson_22', subject_id_1),
    ('lesson_33', subject_id_2),
    ('lesson_44', subject_id_2),
    ('lesson_55', subject_id_3),
    ('lesson_66', subject_id_3)
]

les_isd = []
for value in values:
    cursor.execute(query, value)
    lesson_id = cursor.lastrowid
    les_isd.append(lesson_id)
lesson_id_1 = les_isd[0]
lesson_id_2 = les_isd[1]
lesson_id_3 = les_isd[2]
lesson_id_4 = les_isd[3]
lesson_id_5 = les_isd[4]
lesson_id_6 = les_isd[5]

query = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
values = [
    (1, lesson_id_1, student_id),
    (6, lesson_id_2, student_id),
    (10, lesson_id_3, student_id),
    (7, lesson_id_4, student_id),
    (3, lesson_id_5, student_id),
    (5, lesson_id_6, student_id)
]
cursor.executemany(query, values)

query = "SELECT * FROM marks WHERE student_id = %s"
value = (student_id,)
cursor.execute(query, value)
marks = cursor.fetchall()
print('Marks', marks)

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print("Books:", books)

cursor.execute("""
    SELECT * FROM students
    LEFT JOIN books ON students.id = books.taken_by_student_id
    LEFT JOIN `groups` ON students.group_id = `groups`.id
    LEFT JOIN marks ON students.id = marks.student_id
    LEFT JOIN lessons ON marks.lesson_id = lessons.id
    LEFT JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = %s
    """, (student_id,))
full_data = cursor.fetchall()
print("Full data:", full_data)
