# import calculator
# from calculator import muliplication
# from calculator import *
#
# print(calculator.addition(5, 5))
# print(muliplication(2, 2))
# print(addition(13, 42))


# import random
#
# random_number = random.randint(1, 100)
# print(random_number)
#
# lst = [1, 2, 3, 5, "f", "t"]
# random_el = random.choice(lst)
# print(random_el)

# import datetime

# print(datetime.datetime.now())

# now = datetime.datetime.now().date()
# yesterday = datetime.datetime(2022, 11, 11).date()

# print(type(now), now)
# print(type(yesterday), now)
# print(yesterday - now)

# start = datetime.datetime.now()
#
# a = 0
# for i in range(50_000_000):
#     a += 1
#
# print(datetime.datetime.now() - start)

# print(datetime.datetime.now().date())
#
# date_a = "12/08/2003"
# date_b = "10.11.19"
#
# date_a_correct = datetime.datetime.strptime(date_a, "%d/%m/%Y").date()
# date_b_correct = datetime.datetime.strptime(date_b, "%d.%m.%y").date()
#
# print(date_a_correct)
# print(date_b_correct)
# print(date_b_correct - date_a_correct)

# from termcolor import cprint

# cprint("Hello, World!", color="grey", on_color="on_white", attrs=['bold'])

# Модуль \ Библиотека \ Зависимость   |   Фреймворк

# from decouple import config
#
# passw = config("PASSWORD", cast=int)
# secret_key = config("SECRET_KEY", default="ABCDEFG")
#
#
# print(type(passw), passw)
# print(type(secret_key), secret_key)


def hello(name):
    print(f"Hello {name}")