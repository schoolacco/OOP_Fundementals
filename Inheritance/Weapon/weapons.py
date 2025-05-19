class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.dc = damage_category
    def get_stats(self):
        super().get_stats(self)
        print(f"Damage category: {self.dc}")
        print(f"Crit: {self.damage * 3}")
class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.dc = damage_category
    def get_stats(self):
        super().get_stats(self)
        print(f"Damage category: {self.dc}")
        print(f"Crit: {self.damage*2}")
class Longbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init(name, category, damage, damage_category)
        self.br = bow_range
    def get_stats(self):
        super().get_stats(self)
        print(f"Bow range: {self.br}ft")
class Shortbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init(name, category, damage, damage_category)
        self.br = bow_range
    def get_stats(self):
        super().get_stats(self)
        print(f"Bow range: {self.br}ft")