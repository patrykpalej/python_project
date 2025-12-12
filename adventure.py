class Task:
    def __init__(self, name, task_type, difficulty, success_damage,
                 fail_damage):

        self.name = name
        self.task_type = task_type
        self.difficulty = difficulty
        self.success_damage = success_damage
        self.fail_damage = fail_damage
        self.completed = None
        self.character_assigned = None


class Adventure:
    def __init__(self, team, tasks):
        self.team = team
        self.tasks = tasks

    @property
    def all_alive(self):
        return True if all([team_member.is_alive
                            for team_member in self.team]) else False

    @property
    def __lowest_hp_character(self):
        hp_list = [team_member.hp for team_member in self.team]
        min_hp = min(hp_list)
        team_char_index = hp_list.index(min_hp)
        return self.team[team_char_index]

    def run(self):
        pass
