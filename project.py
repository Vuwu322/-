
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.student_grades:
                    lecturer.student_grades[course].append(grade)
                else:
                    lecturer.student_grades[course] = [grade]
            else:
                return "Ошибка: Оценка должна быть от 0 до 10."
        else:
            return "Ошибка: Лектор не ведет этот курс, или студент на него не записан."

    def get_average_grade(self):
        total_grades = []
        for course_grades in self.grades.values():
            total_grades.extend(course_grades)
        if total_grades:
            return round(sum(total_grades) / len(total_grades), 1)
        else:
            return "Нет оценок за домашние задания"

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов в процессе"
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade if not isinstance(average_grade, str) else average_grade}\n"
            f"Курсы в процессе изучения: {courses_in_progress_str}\n"
            f"Завершенные курсы: {finished_courses_str}"
        )


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def get_average_grade(self):
        total = 0
        count = 0
        for course, grades in self.student_grades.items():
            total += sum(grades)
            count += len(grades)
        if count > 0:
            return round(total / count, 1)
        else:
            return "Пока нет оценок от студентов"

    def __str__(self):
        average_grade = self.get_average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average_grade if not isinstance(average_grade, str) else average_grade}"
        )

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student1 = Student("Ruoy", "Eman", "your_gender")
student2 = Student("Alice", "Smith", "female")

lecturer1 = Lecturer("Some", "Buddy")
lecturer2 = Lecturer("John", "Doe")

reviewer1 = Reviewer("Cool", "Reviewer")
reviewer2 = Reviewer("Jane", "Smith")

student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]
student2.courses_in_progress += ["Python", "Java"]
student2.finished_courses += ["Основы ООП"]

lecturer1.courses_attached += ["Python", "Git"]
lecturer2.courses_attached += ["Java"]

reviewer1.courses_attached += ["Python", "Git"]
reviewer2.courses_attached += ["Java"]


reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student2, "Java", 8)
reviewer2.rate_hw(student2, "Java", 9)

student1.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "Java", 8)
student2.rate_lecturer(lecturer2, "Java", 10)

print("Студент 1:\n", student1)
print("\nСтудент 2:\n", student2)
print("\nЛектор 1:\n", lecturer1)
print("\nЛектор 2:\n", lecturer2)
print("\nРевьюер 1:\n", reviewer1)
print("\nРевьюер 2:\n", reviewer2)

def calculate_average_hw_grade(student_list, course_name):
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

def calculate_average_lecture_grade(lecturer_list, course_name):
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


student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

print("\nСредняя оценка за домашние задания по Python:", calculate_average_hw_grade(student_list, "Python"))
print("Средняя оценка за лекции по Python:", calculate_average_lecture_grade(lecturer_list, "Python"))
print("Средняя оценка за домашние задания по Java:", calculate_average_hw_grade(student_list, "Java"))
print("Средняя оценка за лекции по Java:", calculate_average_lecture_grade(lecturer_list, "Java"))
