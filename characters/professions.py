class Character:
    max_hp = 10.0

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hp = 8.0
        self.strength = 4
        self.intelligence = 4
        self.faith = 4

    def to_json(self):
        return self.__dict__

    def take_damage(self, amount):
        self.hp = max(0, self.hp - max([0, amount]))

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} - {self.race} {self.__class__.__name__}"

    @property
    def is_alive(self):
        return self.hp > 0
