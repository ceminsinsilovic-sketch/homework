import time


class Fighter:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack


def create_fighter():
    name = input("Введите имя бойца: ").strip()

    while not name:
        name = input("Имя не должно быть пустым. Введите имя: ").strip()

    hp = int(input("HP: "))
    attack = int(input("Сила удара: "))

    return Fighter(name, hp, attack)


def show_players(players):
    print("\nСписок бойцов:")

    for i, player in enumerate(players, start=1):
        print(f"{i}. {player.name} — HP: {player.hp}")


def fight(a, b):
    round_number = 1

    print(f"\nНачинается бой: {a.name} против {b.name}!")

    while a.hp > 0 and b.hp > 0:
        print(f"\nРаунд {round_number}")
        damage_a = a.attack
        damage_b = b.attack

        a.hp = max(0, a.hp - damage_b)
        b.hp = max(0, b.hp - damage_a)

        print(f"{a.name} получает удар. Осталось HP: {a.hp}")
        print(f"{b.name} получает удар. Осталось HP: {b.hp}")

        round_number += 1
        time.sleep(1)

    if a.hp == 0 and b.hp == 0:
        print("\nНичья! Оба бойца проиграли.")
    elif a.hp > 0:
        print(f"\n{a.name} победил!")
    else:
        print(f"\n{b.name} победил!")


def remove_dead(players):
    return [player for player in players if player.hp > 0]


players = []

for i in range(2):
    print(f"\nСоздание бойца {i + 1}")
    players.append(create_fighter())

show_players(players)
fight(players[0], players[1])

players = remove_dead(players)

print("\nПосле боя:")
show_players(players)
