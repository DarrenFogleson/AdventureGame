class Enemy:
    def __init__(self, name, hp, damage):
                 self.name = name
                 self.hp = hp
                 self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Dave(Enemy):
        def __init__(self):
            super().__init__(name="Dave", hp=4, damage=5)

class Guard(Enemy):
        def __init__(self):
            super().__init__(name="Guard Jeff", hp=6, damage=9)
