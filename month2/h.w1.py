# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о
# человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который
# был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем
# предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса salary
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к
# стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются
# в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с
# его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.

import random
from random import randint
class Person():
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'I am {self.fullname}, age: {self.age},  is married: {self.is_married}')


class Student(Person):
    marks = {"eng": 4,'rus': 5,"math": 5,}

    def math_mid(self):
        res = 0
        count = 0
        for i in self.marks.values():
            res += i
            count += 1
        return res / count


class Teacher(Person):
    def __init__(self, fullname, age, is_married, salary, experience):
        super().__init__(fullname, age, is_married)
        self.salary = salary
        self.experience = experience

    def full_salary(self):
        if self.experience > 3:
            self.salary += self.salary * 0.05
        print(self.salary)


def create_students():
    res = []
    for i in range(3):
        n = random.randint(1, 5)
        if n == 1:
            n = "era"
        elif n == 2:
            n = "alihan"
        elif n == 3:
            n = "syimyk"
        elif n == 4:
            n = "alihan"
        elif n == 5:
            n = ""
        else:
            pass
        a = random.randint(12, 19)
        a = Student(n, a, True)
        res.append(a)
    return res


for i in create_students():
    i.introduce_myself()
    print(i.math_mid())

stud1 = Person("mura", 15, False)
teacher = Teacher("uchilka", 43, False, 45000, 17)

stud1.introduce_myself()

teacher.full_salary()
teacher.introduce_myself()
create_students()