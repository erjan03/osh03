'''1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
форму.
Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
FYI и т.п.
2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
фразе было использовано. Например: “Money, money, money, it’s always sunny, in
the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
world: 1.
3) Напишите функцию, которая принимает слово и возвращает True, если слово
изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
4) Напишите функцию где мы передаем через аргументы число n как целое
integer, надо вывести целове число в перевернутом виде
например: n = 27, тогда перевёрнутое n это 72
ДОП ЗАДАНИЕ:
5) Напишите функцию -- чат-бот с бесконечным циклом, который
a. Всегда отвечает “Конечно!” на любой вопрос
b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
духе!” Если вызвал функцию, но ничего не передал.
d. В любых других случаях, отвечает “ну и что”'''

# AB = float(input("Введите расстояние A-B в километрах:\n")) 
# AC = float(input("Введите расстояние A-C в милях:\n")) 
# print(f'A-B: {AB/1.61} миль; A-C: {AC*1.61} км.')

def shorter(rvrsleo):
    rvrsleo_dict = rvrsleo.split()
    for i in range(len(rvrsleo_dict)):
        print(rvrsleo_dict[i][0], end = '')
shorter("Кыргызская Рспублика")

# a = ("Money, money, money, it’s always sunny, inthe richmen’s world")
# def dz():
#     print("кол money:", a.count('money') + a.count('Money'), "кол it’s:", a.count('it’s'))
# dz()