from actor import *


class Player(LoadActor):
    def __init__(self):
        super().__init__('aduan', 
                        {'walk': 'aduan_walk', 'stand': 'aduan_stand'}, 
                        (-600, -60, 0), 'player', 30, 100)
        self.actor.setScale(4.5)
