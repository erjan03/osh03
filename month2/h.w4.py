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
        super(Thor, self).__init__(name, health, damage, "tor")

    def apply_super_power(self, boss, heroes):
        tor_point = random.randint(1,7)
        if tor_point == 3 and self.pop > 0:
            self.pop -= 1
            for hero in heroes:
                if hero != self and hero.health > 0:
                    hero.health += boss.damage
            print("boss oglushen")
        else:
            pass

class Golem(Heroes):
    prot = 1
    def __init__(self, name, health, damage):
        super(Golem, self).__init__(name, health, damage, "prot" )
    
    def apply_super_power(self, boss, heroes):
        prot_point = random.randint(1,5)
        if prot_point == 3 and self.prot > 0:
            self.prot -= 1
            for hero in heroes:
                if hero != self and hero.health > 0:
                    hero.health += boss.damage // 5
            print(f"golem prinyal uron", {self.damage // 5}) 
        else:
            pass
class Witcher(Heroes):
    jizn = 1
    def __init__(self, name, health, damage):
        super(Witcher, self).__init__(name, health, damage, "jizh")

    def apply_super_power(self, boss, heroes):
        # jizn_point = random.randint(1,5)
        if self.health == 0 and self.jizn > 0:
            self.jizn -= 1
            for hero in heroes:
                if hero != self and hero.health < 0:
                    hero.health += hero.health
            if hero.health + hero.health:
                Witcher.health == 0
            print(f"Whitcher umer ", {self.health}) 
        else:
            pass
# class Avrora(Heroes):
#     pop = 1
#     def __init__(self, name, health, damage):
#         super(Avrora, self).__init__(name, health, damage, "невидимость")

#     def apply_super_power(self, boss, heroes):
#         avrora_point = random.randint(1,7)
#         if avrora_point == 4 and self.pop > 0:
#             Avrora.health + boss.damage
#         print("Avrora block")   
                
# class Druid(Heroes):
#     angel = 1
#     def __init__(self, name, health, damage):
#         super(Druid, self).__init__(name, health, damage, "angel")

#     def apply_super_power(self, boss, heroes):
#         angel_point = random.randint(1, 10)
#         print(f"ANGEL POINT {angel_point}")
#         if angel_point == 4 and self.angel > 0:
#             self.angel -= 1




# class AntMan(Heroes):
#     obem = random.randint(1, 5)
#     def __init__(self, name, health, damage):
#         super(AntMan, self).__init__(name, health, damage, "obem")

#     def apply_super_power(self, boss, heroes):
#         if self.health == 0 and self.obem > 0:
#             self.obem -= 1
#             for hero in heroes:
#                 if hero != self and hero.health < 0:
#                     hero.health += hero.health
#             if hero.health + hero.health:
#                 AntMan.health == 0
#             print(f"Whitcher umer ", {self.health}) 
#         else:
#             pass

class Superman(Heroes):
    lazer = 1
    def __init__(self, name, health, damage, super_ability):
        super(Superman, self).__init__(name, health, damage, super_ability)

    def apply_super_power(self, boss, heroes):
        prot_point = random.randint(1,20)
        if prot_point == 7 and self.lazer > 0:
            boss.health == 0
        print("Boss Umer")

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
    boss = Boss("Сыймык", 5000, 50)
    warrior = Warrior("Алихан", 270, 50)
    magic = Magic("Мура", 280, 20)
    medic = Medic("Эра", 220, 5)
    medic2 = Medic("Абу", 180, 2)
    voin = Berserk("берс", 250, 15)
    voin1 = Thor("tor", 250, 20)
    voin2 = Golem("Голем", 400, 2)
    voin3 = Witcher("witch", 200, 0)
    # voin4 = Avrora("Avrora", 200, 10)
    # voin5 = AntMan("муравей", 150, 10)
    # voin6 = Druid("Ангел", 210, 10)
    voin7 = Superman("Superman", 300, 15, "lazer")
    heroes = [warrior, magic, medic, medic2, voin, voin1, voin2, voin3, voin7 ]#voin4, voin5, voin6]

    print_statistic(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()

