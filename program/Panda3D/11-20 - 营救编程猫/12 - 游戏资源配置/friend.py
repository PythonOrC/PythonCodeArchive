from actor import *


class Friend(LoadActor):
    def __init__(self):
        super().__init__('codemao',
                         {'walk': 'codemao_walk', 'stand': 'codemao_stand'},
                         (450, 20, 0), 'friend', 25, 100)
        self.actor.setScale(0.6)
