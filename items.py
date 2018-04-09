class Item():
    """The Class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Fags(Item):
    def__init__(self, amt):
       self.amt = amt
       super().__init__(name="Fags",
                         description="A cylinder made of paper filled with tobacco that gets smoked.".format(str(self.amt)),
                         value=self.amt)
class Weapon(Item):
    def __init__(self, name, description, value, damage
                 self.damage = damage
                 super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fists(weapon):
    def __init__(self):
        super().__init__(name="Fists"
                         description="Yer bloody fists.",
                         value=0,
                         damage=2)

class Shank(weapon):
    def __init__(self):
        super().__init__(name="Shank"
                         description="A shank formed from a toothbrush that you found on yer mate Dave's dead body.",
                         value=2,
                         damage=5)

class Baton(weapon):
    def __init__(self):
        super().__init__(name="Guard's Baton"
                         description="A baton you found on freindly Guard Jeff you just murdured in cold blood you monster.",
                         value=10,
                         damage=10)
