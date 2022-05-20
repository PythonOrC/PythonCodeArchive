from actor import *


class EnemyWoodmen(LoadActor):
    def __init__(self):
        super().__init__('woodmen',
                         {'walk': 'woodmen_walk',
                             'stand': 'woodmen_stand', "die": 'woodmen_die', 'attack': 'woodmen_attack'},
                         (-0, -100, 0), 'wwoodmen', 10, 100)
        self.actor.setScale(1.2)


class EnemyNeedle(LoadActor):
    def __init__(self):
        super().__init__('GroundNeedle',
                         {'motion': 'GroundNeedle_motion',
                             'stop': 'GroundNeedle_stop'},
                         (270, 0, -2), 'wwoodmen', 5, 100)
        self.actor.setScale(1.2)
