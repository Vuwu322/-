
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 <= grade <= 10:
                if course in lecturer.student_grades:
                    lecturer.student_grades[course].append(grade)
                else:
                    lecturer.student_grades[course] = [grade]
            else:
                return "Ошибка: Оценка должна быть от 0 до 10."
        else:
            return 'Ошибка: Лектор не ведет этот курс, или студент на него не записан.'

    def __str__(self):
        courses_in_progress_string = ", ".join(self.courses_in_progress)
        finished_courses_string = ", ".join(self.finished_courses)
        grades_string = ""
        for course, grades in self.grades.items():
            grades_string += f"{course}: {', '.join(map(str, grades))}\n"

        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.calculate_average_grade()}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}\n' \
              f'Оценки:\n{grades_string}'
        return res

    def calculate_average_grade(self):
        total_grades = []
        for course in self.grades:
            total_grades.extend(self.grades[course])
        if total_grades:
            return round(sum(total_grades) / len(total_grades), 1)
        else:
            return "Нет оценок"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.calculate_average_grade() < other.calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_average_grade()}'

    def calculate_average_grade(self):
        total_grades = []
        for course in self.student_grades:
            total_grades.extend(self.student_grades[course])
        if total_grades:
            return round(sum(total_grades) / len(total_grades), 1)
        else:
            return "Нет оценок"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.calculate_average_grade() < other.calculate_average_grade()

class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Some', 'Buddy', 'your_gender')
student3 = Student('Alice', 'Wonder', 'female')
student4 = Student('Bob', 'Builder', 'male')

lecturer1 = Lecturer('John', 'Smith')
lecturer2 = Lecturer('Jane', 'Doe')
lecturer3 = Lecturer('Michael', 'Brown')
lecturer4 = Lecturer('Emily', 'Wilson')

reviewer1 = Reviewer('Cool', 'Reviewer')
reviewer2 = Reviewer('Jane', 'Smith')
reviewer3 = Reviewer('David', 'Lee')
reviewer4 = Reviewer('Sarah', 'Jones')

# Определение курсов и их прохождение
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Java', 'Git']
student2.finished_courses += ['Введение в программирование']
student3.courses_in_progress += ['Python', 'Data Science']
student4.courses_in_progress += ['Java', 'Databases']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Java']
lecturer3.courses_attached += ['Data Science']
lecturer4.courses_attached += ['Databases']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']
reviewer3.courses_attached += ['Data Science']
reviewer4.courses_attached += ['Databases']

# Оценивание домашних заданий
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer3.rate_hw(student3, 'Data Science', 9)
reviewer3.rate_hw(student3, 'Data Science', 10)
reviewer4.rate_hw(student4, 'Databases', 7)
reviewer4.rate_hw(student4, 'Databases', 8)

# Оценивание лекций
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Java", 8)
student2.rate_lecturer(lecturer2, "Java", 9)
student3.rate_lecturer(lecturer3, "Data Science", 10)
student3.rate_lecturer(lecturer3, "Data Science", 9)
student4.rate_lecturer(lecturer4, "Databases", 7)
student4.rate_lecturer(lecturer4, "Databases", 8)

# Вывод информации об экземплярах
print("Студент 1:\n", student1)
print("\nСтудент 2:\n", student2)
print("Студент 3:\n", student3)
print("\nСтудент 4:\n", student4)
print("\nЛектор 1:\n", lecturer1)
print("\nЛектор 2:\n", lecturer2)
print("Лектор 3:\n", lecturer3)
print("\nЛектор 4:\n", lecturer4)
print("\nРевьюер 1:\n", reviewer1)
print("\nРевьюер 2:\n", reviewer2)
print("Ревьюер 3:\n", reviewer3)
print("\nРевьюер 4:\n", reviewer4)

# Сравнение студентов
print("\nСтудент 1 < Студент 2:", student1 < student2)
print("Лектор 1 < Лектор 2:", lecturer1 < lecturer2)

def calculate_average_hw_grade_for_course(student_list, course_name):
    total_grade = 0
    student_count = 0
    for student in student_list:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            student_count += len(student.grades[course_name])
    if student_count > 0:
        return round(total_grade / student_count, 1)
    else:
        return "Нет оценок за домашние задания по этому курсу"

def calculate_average_lecture_grade_for_course(lecturer_list, course_name):
    total_grade = 0
    lecturer_count = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.student_grades:
            total_grade += sum(lecturer.student_grades[course_name])
            lecturer_count += len(lecturer.student_grades[course_name])

    if lecturer_count > 0:
        return round(total_grade / lecturer_count, 1)
    else:
        return "Нет оценок за лекции по этому курсу"


student_list = [student1, student2, student3, student4]
lecturer_list = [lecturer1, lecturer2, lecturer3, lecturer4]


print("\nСредняя оценка за домашние задания по Python:", calculate_average_hw_grade_for_course(student_list, "Python"))
print("Средняя оценка за лекции по Python:", calculate_average_lecture_grade_for_course(lecturer_list, "Python"))
print("Средняя оценка за домашние задания по Java:", calculate_average_hw_grade_for_course(student_list, "Java"))
print("Средняя оценка за лекции по Java:", calculate_average_lecture_grade_for_course(lecturer_list, "Java"))
print("Средняя оценка за домашние задания по Data Science:", calculate_average_hw_grade_for_course(student_list, "Data Science"))
print("Средняя оценка за лекции по Data Science:", calculate_average_lecture_grade_for_course(lecturer_list, "Data Science"))
print("Средняя оценка за домашние задания по Databases:", calculate_average_hw_grade_for_course(student_list, "Databases"))
print("Средняя оценка за лекции по Databases:", calculate_average_lecture_grade_for_course(lecturer_list, "Databases"))
