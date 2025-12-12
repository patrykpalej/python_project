from utils import dice_roll, expected_dice_roll
from characters.races import Human, Elf, Orc


class Character:
    max_hp = 10

    def __init__(self, name, race):

        self.name = name
        self.race = race
        self.hp = 8.0
        self.strength = 4
        self.intelligence = 4
        self.faith = 4

        self._apply_race()

    def to_json(self):
        return self.__dict__

    @property
    def is_alice(self):
        return self.hp > 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} - {self.race} {self.__class__.__name__}"

    def take_damage(self, damage_value):
        self.hp = max(0, self.hp - damage_value)

    def heal(self, heal_value):
        self.hp = min(self.max_hp, self.hp + heal_value)

    def _apply_race(self):
        stats_modified = self.race.modify_statistics(self.__dict__)
        self.strength = stats_modified["strength"]
        self.intelligence = stats_modified["intelligence"]
        self.faith = stats_modified["faith"]


class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength += 2
        self.intelligence -= 1

    def expected_contribution(self, task_type):
        return (self.strength + expected_dice_roll
                if task_type == "combat" else 2 + expected_dice_roll)

    def contribute(self, task_type):
        return (self.strength + dice_roll()
                if task_type == "combat" else 2 + dice_roll())


class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 1
        self.intelligence += 2
        self.faith += 1
        self.mana = 5.0

    def expected_contribution(self, task_type):
        return (self.mana // 2 + self.intelligence + expected_dice_roll
                if task_type == "magic" else 2 + expected_dice_roll)

    def contribute(self, task_type):
        if task_type == "magic":
            result = self.mana // 2 + self.intelligence + dice_roll()
            self.__spend_mana()
        else:
            result = 2 + dice_roll()
        return result

    def __spend_mana(self):
        self.mana = max([0.0, self.mana-1])


class Priest(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 2
        self.intelligence += 1
        self.faith += 3

        self.mana = 5.0

    def expected_contribution(self, task_type):
        return (self.faith + expected_dice_roll
                if task_type in ("holly", "support") else 1 + expected_dice_roll)

    def contribute(self, task_type):
        return (self.faith + dice_roll()
                if task_type in ("holly", "support") else 1 + dice_roll())

    def heal_ally(self, team_member):
        if self.mana > 0:
            heal_amount = self.faith / 5
            team_member.heal(heal_amount)
            self.mana = max([0, self.mana-(heal_amount * 0.1)])
