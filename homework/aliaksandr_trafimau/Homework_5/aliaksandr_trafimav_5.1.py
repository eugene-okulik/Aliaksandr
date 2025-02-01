# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print (name, last_name, city, phone, country)

# Task 2
a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

#Result 1
n1=int(a[-2:])+10
n2=int(b[-3:])+10
n3=int(c[-1:])+10
print('result1 :', n1+n2+n3)

#Result 2
c1 = int(a[a.index('42'):]) + 10
c2 = int(b[b.index('514'):]) + 10
c3 = int(c[c.index('9'):]) + 10
print('result2 :', c1+c2+c3)

#Result 3
d1 = int(a[a.index(':') + 2:]) + 10
d2 = int(b[b.index(':') + 2:]) + 10
d3 = int(c[c.index(':') + 2:]) + 10
print('result3 :', d1+d2+d3)

#Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

#Result 1
g1 = ', '.join(students)
g2 = ', '.join(subjects)
print('Students ' + g1 + ' study these subjects: ' + g2)

#Result 2
print('Students ' + ', '.join(students) + ' study these subjects: ' + ', '.join(subjects))