#чем меньше процентов хп у персонажа тем сильнее его удар, но есть лимит, если
#меньше 20% хп, то баф снимается. Мы должны считать получаемый урон и сумировать его
#а потом сравнивать, если урон нанёс 1% от максимального количества хп, то и сила удара
#поднимается на 1%

class Fighters:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.attack = self.base_attack * level
        self.health_points = self.base_health_points * level
        
    def attack_method(self, target: "Fighters"):
        target.got_damage(damage=self.attack)
    def add_hp(self):
        if self.is_alive:
            self.health_points += self.max_hp / 2
    def got_damage(self, damage):
        damage = damage * (100 - self.defence_emth) / 100
        round_damage = round(damage)
        self.health_points -= round_damage
    def berserker(self, target: "Fighters"):
        pass
    @property
    def max_level_control(self):
        if self.level > 3:
            self.level = 3
    def is_alive(self)->bool:
        return self.health_points > 0
    def is_alive_str(self)->str:
        if self.is_alive() == True:
            return "is alive"
        return "is dead"
    @property
    def defence_emth(self)->int:
        self.defence = self.base_defence * self.level
        return self.defence
    @property
    def max_hp(self)->int:
        return self.base_health_points * self.level
    def hp_precent(self)->int:
        return 100 * self.health_points / self.max_hp
    def __str__(self):
        return f"name ({self.name}) power ({self.attack}), HP ({self.health_points})"

class Ork(Fighters):
    base_attack = 11
    base_health_points = 70
    base_defence = 11

    @property
    def defence_emth(self)->int:
        defence = super().defence_emth
        if self.health_points < 50:
            defence *= 3
        return defence

ork = Ork(name="Ork", level=1)

class Nord(Fighters):
    base_attack = 16
    base_health_points = 100
    base_defence = 10
    
    def attack_method(self, target: "Fighters"):
        attack = self.attack
        if target.hp_precent() < 30:
            attack = self.attack * 2
        target.got_damage(damage=attack)

nord = Nord(name="Nord", level=1)

def Fight(character1: Fighters, character2: Fighters):
    while character1.is_alive() and character2.is_alive():
        character2.attack_method(target=character1)
        if character1.is_alive() == False:
            character2.level += 1
            character2.add_hp()
        elif character1.is_alive():
            character1.attack_method(target=character2)
        elif character2.is_alive() == False:
            character1.level += 1
            character1.add_hp()

    print(f"{character2.name} {character2.is_alive_str()}, {character2.name}(level: {character2.level}, hp: {character2.health_points})")
    print(f"{character1.name} {character1.is_alive_str()}, {character1.name}(level: {character1.level}, hp: {character1.health_points})")

Fight(nord, ork)
