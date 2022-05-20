from actor import *
import random


class EnemyWoodmen(LoadActor):
    def __init__(self, pos):
        super().__init__('woodmen',
                         {'walk': 'woodmen_walk',
                             'stand': 'woodmen_stand', "die": 'woodmen_die', 'attack': 'woodmen_attack'},
                         pos, 'woodmen', 10, 1)
        self.actor.setScale(1.2)
        self.acceleration = 100
        base.pusher.addCollider(self.collider, self.actor)
        base.cTrav.addCollider(self.collider, base.pusher)
        self.default_orientation = Vec2(0, -1)
        self.change_orientation = Vec2(0, -1)
        self.detection_distance = 100
        self.acceleration_chase = 400
        self.actor.enableBlend()
        self.harm_value = -5
        self.harm_interval = 0.5
        self.organ_crack_state = False

    def woodmen_move(self, player, dt, codemao):
        LoadActor.move(self, dt)
        if not self.organ_crack_state:
            position_vec3 = player.actor.getPos()-self.actor.getPos()
            position_vec2 = position_vec3.getXy()
            distance_to_player = position_vec2.length()
            if distance_to_player > self.detection_distance:
                self.walking = True
                self.heading = self.default_orientation.signedAngleDeg(
                    self.change_orientation)
                self.actor.setH(self.heading)
                self.velocity.addY(self.acceleration*dt)
                self.actor.setControlEffect('walk', 0.7)
                self.actor.setControlEffect('attack', 0.3)
            elif distance_to_player < self.detection_distance and distance_to_player > 30:
                self.walking = True
                self.heading = self.default_orientation.signedAngleDeg(
                    position_vec2)
                self.actor.setH(self.heading)
                self.velocity.addY(self.acceleration_chase*dt)
                self.actor.setControlEffect('walk', 0.9)
                self.actor.setControlEffect('attack', 0.1)
            else:
                self.walking = False
                self.heading = self.default_orientation.signedAngleDeg(
                    position_vec2)
                self.actor.setH(self.heading)
                self.actor.setControlEffect('walk', 0)
                self.actor.setControlEffect('attack', 1)
                self.harm_interval -= dt
                if self.harm_interval <= 0:
                    player.count_health(self.harm_value)
                    print('player', player.health)
                    self.harm_interval = random.uniform(0.5, 1)
        else:
            position_to_codemao_vec3 = codemao.actor.getPos()-self.actor.getPos()
            position_to_codemao_vec2 = position_to_codemao_vec3.getXy()
            distance_to_codemao = position_to_codemao_vec2.length()
            if distance_to_codemao > self.detection_distance:
                self.walking = True
                self.heading = self.default_orientation.signedAngleDeg(
                    self.change_orientation)
                self.actor.setH(self.heading)
                self.velocity.addY(self.acceleration*dt)
                self.actor.setControlEffect('walk', 0.7)
                self.actor.setControlEffect('attack', 0.3)
            elif distance_to_codemao < self.detection_distance and distance_to_codemao > 50:
                self.walking = True
                self.heading = self.default_orientation.signedAngleDeg(
                    position_to_codemao_vec2)
                self.actor.setH(self.heading)
                self.velocity.addY(self.acceleration_chase*dt)
                self.actor.setControlEffect('walk', 0.9)
                self.actor.setControlEffect('attack', 0.1)
            else:
                self.walking = False
                codemao.walk_state = False
                self.heading = self.default_orientation.signedAngleDeg(
                    position_to_codemao_vec2)
                self.actor.setH(self.heading)
                self.actor.setControlEffect('walk', 0)
                self.actor.setControlEffect('attack', 1)
                self.harm_interval -= dt
                if self.harm_interval <= 0:
                    codemao.count_health(self.harm_value)
                    print('codemao', codemao.health)
                    self.harm_interval = random.uniform(0.5, 1)
        if self.walking:
            walk_control = self.actor.getAnimControl('walk')
            if not walk_control.isPlaying():
                self.actor.loop('walk')
                self.actor.loop('attack')
        else:
            self.actor.loop('stand')


class EnemyNeedle(LoadActor):
    def __init__(self):
        super().__init__('GroundNeedle',
                         {'motion': 'GroundNeedle_motion',
                             'stop': 'GroundNeedle_stop'},
                         (270, 0, -2), 'wwoodmen', 5, 100)
        self.actor.setScale(1.2)
        self.actor.loop('motion')
        needle_node = NodePath('needlelist')
        for i in range(50, 220, 20):
            needle = needle_node.attachNewNode('needle')
            needle.setPos(80, i, 0)
            self.actor.instanceTo(needle)
        for i in range(-220, -50, 20):
            needle = needle_node.attachNewNode('needle')
            needle.setPos(40, i, 0)
            self.actor.instanceTo(needle)
        needle_node.reparentTo((render))
        self.collider.removeNode()
        needle_solid_1 = CollisionCapsule(250, 220, 0, 350, 40, 0, 5)
        needle_node_1 = CollisionNode('needle')
        needle_node_1.addSolid(needle_solid_1)
        needle_1 = render.attachNewNode(needle_node_1)

        needle_solid_2 = CollisionCapsule(310, -50, 0, 310, -230, 0, 5)
        needle_node_2 = CollisionNode('needle')
        needle_node_2.addSolid(needle_solid_2)
        needle_2 = render.attachNewNode(needle_node_2)

        self.harm_value = -2
        self.harm_interval = 0.6

        self.hue_queue = CollisionHandlerQueue()
        base.cTrav.addCollider(needle_1, self.hue_queue)
        base.cTrav.addCollider(needle_2, self.hue_queue)

        mask = BitMask32()
        needle_node_1.setIntoCollideMask(mask)
        mask = BitMask32()
        needle_node_2.setIntoCollideMask(mask)

    def attack(self, player, dt):
        if self.hue_queue.getNumEntries() > 0:
            self.hue_queue.sortEntries()
            hue_information = self.hue_queue.getEntry(0)
            if hue_information.getIntoNode().getName() == 'player':
                self.harm_interval -= dt
                if self.harm_interval <= 0:
                    player.count_health(self.harm_value)
                    print('player', player.health)
                    self.harm_interval = random.uniform(0.6, 1)
