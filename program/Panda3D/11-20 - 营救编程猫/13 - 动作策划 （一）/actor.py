from direct.actor.Actor import Actor
from panda3d.core import *


class LoadActor(Actor):
    def __init__(self, modelName, animsName, pos, colliderName, max_speed, max_health):
        super().__init__()
        self.actor = Actor(modelName, animsName)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)
        capsule = CollisionSphere(0, 0, 0, 5)
        collider_node = CollisionNode(colliderName)
        collider_node.addSolid(capsule)
        self.collider = self.actor.attachNewNode(collider_node)
        self.max_speed = max_speed
        self.velocity = Vec3(0, 0, 0)
        self.NeAcc = 500
        self.walking = False
        self.max_health = max_health
        self.health = max_health

    def move(self, dt):
        speed = self.velocity.length()
        if speed > self.max_speed:
            self.velocity.normalize()
            self.velocity *= self.max_speed
            speed = self.max_speed
        if not self.walking:
            neSpeed = self.NeAcc * dt
            if neSpeed > speed:
                self.velocity = Vec3(0, 0, 0)
            else:
                slow_speed = -self.velocity
                slow_speed.normalize()
                slow_speed *= neSpeed
                self.velocity += slow_speed
        self.actor.setY(self.actor, -(self.velocity * dt).length())

    def count_health(self, health_change):
        self.health += health_change
        if self.health >= self.max_health:
            self.health = self.max_health

    def clean_up(self):
        if self.collider is not None:
            base.cTrav.removeCollider(self.collider)
            self.collider = None
        if self.actor is not None:
            self.actor.cleanup()
            self.actor.removeNode()
            self.actor = None
