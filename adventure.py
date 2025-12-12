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
