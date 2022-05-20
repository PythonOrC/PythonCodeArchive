from actor import *
import random


class Player(LoadActor):
    def __init__(self):
        super().__init__('aduan',
                         {'walk': 'aduan_walk', 'stand': 'aduan_stand'},
                         (-600, -60, 0), 'player', 20, 100)
        self.actor.setScale(4.5)
        self.acceleration = 100
        base.pusher.addCollider(self.collider, self.actor)
        base.cTrav.addCollider(self.collider, base.pusher)
        self.ray = CollisionRay(0, 0, 0, 0, -1, 0)
        rayNode = CollisionNode('playerRay')
        rayNode.addSolid(self.ray)
        self.ray_collision = self.actor.attachNewNode(rayNode)
        mask = BitMask32()
        mask.setBit(0)
        mask.setBit(2)
        self.collider.node().setIntoCollideMask(mask)
        mask = BitMask32()
        mask.setBit(0)
        self.collider.node().setFromCollideMask(mask)

        mask = BitMask32()
        self.ray_collision.node().setIntoCollideMask(mask)
        mask = BitMask32()
        mask.setBit(1)
        self.ray_collision.node().setFromCollideMask(mask)

        self.ray_queue = CollisionHandlerQueue()
        base.cTrav.addCollider(self.ray_collision, self.ray_queue)

        self.laser_weapon = loader.loadModel('laser')
        self.laser_weapon.reparentTo(self.actor)
        self.harm_value = -3
        self.harm_interval = 0.5
        self.transfer_woodmen_life = 1

    def aduan_move(self, keys, woodmen, dt):
        LoadActor.move(self, dt)
        self.walking = False
        self.laser_weapon.setSy(8/13)
        if keys['up']:
            self.velocity.addY(self.acceleration*dt)
            self.walking = True
            base.cam.setPos(self.actor, (0, 60, 150))
            base.cam.setHpr(self.actor, (180, -65, 0))
        if keys['left']:
            self.actor.setH(self.actor.getH()+0.2)
            self.walking = True
            base.cam.setPos(self.actor, (0, 60, 150))
            base.cam.setHpr(self.actor, (180, -65, 0))
            self.velocity = Vec3(0, 0, 0)
        if keys['right']:
            self.actor.setH(self.actor.getH()-0.2)
            self.walking = True
            base.cam.setPos(self.actor, (0, 60, 150))
            base.cam.setHpr(self.actor, (180, -65, 0))
            self.velocity = Vec3(0, 0, 0)
        if self.walking:
            walk_control = self.actor.getAnimControl('walk')
            if not walk_control.isPlaying():
                self.actor.loop('walk')
        else:
            self.actor.loop('stand')
        if keys['shoot']:
            if self.ray_queue.getNumEntries() > 0:
                self.ray_queue.sortEntries()
                ray_information = self.ray_queue.getEntry(0)
                collision_position = ray_information.getSurfacePoint(render)
                collision_distance = (
                    collision_position - self.actor.getPos()).length()
                self.laser_weapon.setSy(collision_distance/13)
                if ray_information.getIntoNodePath() == woodmen.collider:
                    self.harm_interval -= dt
                    if self.harm_interval <= 0:
                        woodmen.count_health(self.harm_value)
                        print(woodmen.health)
                        self.harm_interval = random.uniform(0.6, 1.2)
                        self.transfer_woodmen_life = woodmen.health
