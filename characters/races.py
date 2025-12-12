
class Race:
    def __init__(self, name, strength_mod, intelligence_mod, faith_mod):
        self.name = name
        self.strength_mod = strength_mod
        self.intelligence_mod = intelligence_mod
        self.faith_mod = faith_mod

    def modify_statistics(self, stats_dict):
        stats_dict["strength"] += self.strength_mod
        stats_dict["intelligence"] += self.intelligence_mod
        stats_dict["faith"] += self.faith_mod
        return stats_dict


class Human(Race):
    def __init__(self):
        super().__init__("Human", 1, 1, 1)


class Elf(Race):
    def __init__(self):
        super().__init__("Elf", -1, 2, 0)


class Orc(Race):
    def __init__(self):
        super().__init__("Orc", 2, -1, -1)


stats_base = {
    "strength": 4,
    "intelligence": 4,
    "faith": 4
}

if __name__ == "__main__":
    human = Human()
    print(human.__dict__)
    print(human.modify_statistics(stats_base.copy()))

    elf = Elf()
    print(elf.__dict__)
    print(elf.modify_statistics(stats_base.copy()))

    orc = Orc()
    print(orc.__dict__)
    print(orc.modify_statistics(stats_base.copy()))
