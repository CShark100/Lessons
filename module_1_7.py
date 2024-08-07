# Базовые структуры данных.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)     # сортировка студентов
students_list = list (students)     # преобразование имен в список
num = 0
grades_avg = [sum(grades[num])/len(grades[num]), sum(grades[num+1])/len(grades[num+1]), sum(grades[num+2])/len(grades[num+2]), sum(grades[num+3])/len(grades[num+3]), sum(grades[num+4])/len(grades[num+4]) ]
dict_1 = dict(zip(students_list, grades_avg))       # преобразование списков в словарь
print(dict_1)

