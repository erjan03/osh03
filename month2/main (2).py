import random


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super().__str__() + f" defence: {self.__defence}"


class Heroes(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Heroes, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Heroes):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_power(self, boss, heroes):
        coef = random.randint(1, 5)
        boss.health -= self.damage * coef
        print(f"CRITICAL_DAMAGE {self.damage * coef}")


class Magic(Heroes):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 11)
        print(f"BOOST POINT {boost_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.damage += boost_point


class Medic(Heroes):
    def __init__(self, name, health, damage):
        super(Medic, self).__init__(name, health, damage, "HEAL")

    def apply_super_power(self, boss, heroes):
        heal_point = random.randint(5, 11)
        print(f"HEAL POINT {heal_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.health += heal_point
#
#
class Druid(Heroes):
    def __init__(self, name, health, damage):
        super(Druid, self).__init__(name, health, damage, "prizvat")

    def apply_super_power(self, boss, heroes):
        prz = random.choice['angel', 'voron']
        if prz == random.choice == 'angel':
            print(f'prizval {prz} = {5}')

        elif prz == random.choice == 'voron':
            print(f'prizval {prz} = {25}')
            for hero in heroes:
                if hero != self and boss.damage > 0:
                    boss.damage += prz


class Berserk(Heroes):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, "vozvrat")

    def apply_super_power(self, boss, heroes, ):
        coef = random.randint(1, 3)
        boss.health -= self.damage // coef
        print(f"berserk {self.damage // coef}")


class Thor(Heroes):
    pop = 1
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, "Thor")

    def apply_super_power(self, boss, heroes):
        tor_point = random.randint(1,7)
        if tor_point == 3 and self.pop > 0:
            self.pop -= 1
            for hero in heroes:
                if hero != self and hero.health > 0:
                    hero.health += boss.damage
            print("???????? ??????????????")
        else:
            pass


round_counter = 0


def print_statistic(boss, heroes):
    print(f'_____________ ROUND {round_counter} _____________')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_power(boss, heroes)

    print_statistic(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!")

    return all_heroes_dead


def start_game():
    boss = Boss("????????????", 1000, 50)

    warrior = Warrior("????????????", 270, 10)
    magic = Magic("????????", 280, 20)
    medic = Medic("??????", 220, 5)
    medic2 = Medic("??????", 180, 2)
    voin1 = Berserk('bersrek', 300, 20)
    # voin2 = Druid (200, 20)
    voin3 = Thor("Thor", 250, 20)

    heroes = [warrior, magic, medic,  voin1 , voin3 ]

    print_statistic(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
