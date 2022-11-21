# Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# Добавить сеттеры и геттеры к существующим атрибутам.
# Добавить в класс Computer метод make_computations, в котором бы выполнялись
# арифметические вычисления с атрибутами объекта cpu и memory.
# Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# Добавить сеттеры и геттеры к существующему атрибуту.
# Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number,
# в котором бы распечатывалась симуляция звонка в зависимости от переданного номера симкарты 
# (например: если при вызове метода передать число 1 и номер телефона,
# распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
# Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы
# распечатывал симуляцию проложения маршрута до локации.

# В каждом классе переопределить магический метод __str__ которые бы возвращали полную
# информацию об объекте.
# Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было
# сравнивать между собой объекты, по атрибуту memory.
# Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# Распечатать информацию о созданных объектах
# Опробовать все возможные методы каждого объекта (например: use_gps и тд.)
class Computer():
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, value):
        self.__memory = value
    
    def make_computations(self,cpu,memory):
        pass
    def __add__(self, other):
        return self.__cpu + other.__memory

    def __str__(self):
        return super().__str__() 


    def call(self, sim_card_number, call_to_number):
        s = (f"call number: {sim_card_number},{call_to_number}")
        return s

    def use_gps(self,cpu,memory,location):
        return ("right", "left", "stop") 

class Phone():
    def __init__(self,sim):
        self.__sim = sim

    @property
    def s_c_list(self):
        return self.__sim
    @s_c_list.setter
    def s_c_list(self, value):
        self.__memory = value

    def call(self, sim_card_number, call_to_number):
        s = (f"call number: {sim_card_number},{call_to_number}")
        return s
    def __str__(self):
        return super().__str__() 

class SmartPhone(Computer,Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, self.__sim)

    def use_gps(self,cpu,memory,location):
        s = ("right","left","stop")
        return s
     
comp = Computer(1,2)
tel = Phone("Apple")
smart = SmartPhone(2,3)
smart1 = SmartPhone("hp", "22")

Computer.make_computations()
Computer.call(1)
Computer.use_gps()
Computer.__add__()
Computer.__str__()
Phone.call()
Phone.__str__()
SmartPhone.use_gps()
SmartPhone.__str__()

