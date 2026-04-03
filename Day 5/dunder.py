class Monster:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

monster = Monster(100, 10)
print(monster.health)        