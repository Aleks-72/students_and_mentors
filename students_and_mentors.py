class Student:
    items = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.items.append(self)
        
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached  and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        all_grades = 0
        count = []
        for course in self.grades:
            count += self.grades[course]
        for grade in count:
            all_grades += grade
        avg_grades = all_grades / len(count)
        return avg_grades
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
    
    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() < other.avg_grades()
        else:
            return "Ошибка"
                
    def __le__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() <= other.avg_grades()
        else:
            return "Ошибка"
            
    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() == other.avg_grades()
        else:
            return "Ошибка"
            
    def __ne__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() != other.avg_grades()
        else:
            return "Ошибка"
            
    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() > other.avg_grades()
        else:
            return "Ошибка"
            
    def __ge__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.avg_grades() >= other.avg_grades()
        else:
            return "Ошибка"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.items.append(self)

    def avg_grades(self):
        all_grades = 0
        count = []
        for course in self.grades:
            count += self.grades[course]
        for grade in count:
            all_grades += grade
        avg_grades = all_grades / len(count)
        return avg_grades

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades()}'
    
    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() < other.avg_grades()
        else:
            return "Ошибка"
                
    def __le__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() <= other.avg_grades()
        else:
            return "Ошибка"
            
    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() == other.avg_grades()
        else:
            return "Ошибка"
            
    def __ne__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() != other.avg_grades()
        else:
            return "Ошибка"
            
    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() > other.avg_grades()
        else:
            return "Ошибка"
            
    def __ge__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.avg_grades() >= other.avg_grades()
        else:
            return "Ошибка"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}'

student1 = Student('Петр', 'Иванов', 'Мужской')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['C++']
 
student2 = Student('Иван', 'Сидоров', 'Мужской')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['C++']
student2.finished_courses += ['Java']

lecturer1 = Lecturer('Владимир', 'Дронов')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']

lecturer2 = Lecturer('Ольга', 'Шмидт')
lecturer2.courses_attached += ['C++']
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Владимир', 'Дронов')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']

reviewer2 = Reviewer('Ольга', 'Шмидт')
reviewer2.courses_attached += ['C++']

student1.rate_lect(lecturer1, 'Python', 9)
student1.rate_lect(lecturer1, 'Python', 8)
student1.rate_lect(lecturer1, 'Java', 5)
student2.rate_lect(lecturer2, 'C++', 6)

student2.rate_lect(lecturer2, 'C++', 6)
student2.rate_lect(lecturer2, 'C++', 9)
student2.rate_lect(lecturer2, 'Python', 8)
student2.rate_lect(lecturer2, 'Python', 10)
student2.rate_lect(lecturer1, 'Java', 9)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student1, 'Java', 5)
reviewer1.rate_hw(student1, 'Java', 9)

reviewer2.rate_hw(student2, 'C++', 9)
reviewer2.rate_hw(student2, 'C++', 5)
reviewer2.rate_hw(student2, 'C++', 9)

def avg_rate_student(student_list, course_name_student):
    all_grades = []
    for i in range(len(student_list)):
        if course_name_student in student_list[i].grades:
            all_grades += student_list[i].grades[course_name_student]
        else:
            continue
    summ = 0
    for grade in all_grades:
        summ += grade
    avg_grades = summ / len(all_grades)
    result = f'Средняя оценка студентов по курсу {course_name_student}: {avg_grades}'
    return result

def avg_rate_lecturer(lecturer_list, course_name):
    all_grades = []
    summ = 0
    for i in range(len(lecturer_list)):
        if course_name in lecturer_list[i].grades:
            all_grades += lecturer_list[i].grades[course_name]
        else:
            continue
    for grade in all_grades:
        summ += grade
    avg_grades = summ / len(all_grades)
    result = f'Средняя оценка лекторов за лекции по курсу {course_name}: {avg_grades}'
    return result

print(avg_rate_student(Student.items, 'Java'))
print(avg_rate_lecturer(Lecturer.items, 'Java'))
