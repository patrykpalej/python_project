from characters.professions import Warrior, Wizard, Priest
from characters.races import Human, Elf, Orc
from initialization import initialize_team, initialize_tasks

from adventure import Adventure


team_composition = {
    Warrior: 2,
    Wizard: 2,
    Priest: 1
}
available_races = [Human, Elf, Orc]
n_tasks = 5

team = initialize_team(team_composition, available_races)
tasks = initialize_tasks(n_tasks)

adv = Adventure(team, tasks)
adv.run()
