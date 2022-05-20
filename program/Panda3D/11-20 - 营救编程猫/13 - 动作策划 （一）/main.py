from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from player import *
from friend import *
from enemy import *
from creat_fog import *


class Config(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.font = loader.loadFont('font.ttc')
        self.setup()
        base.pusher = CollisionHandlerPusher()
        base.cTrav = CollisionTraverser()
        base.pusher.setHorizontal(True)
        base.pusher.add_in_pattern('%fn-into-%in')

    def setup(self):
        self.window_properties(1400, 1000)
        self.start_dialog = self.create_dialog(
            frame_size=(-1.41, 1.41, -1.01, 1.01), pos=(0, 0, 0), color=(1, 1, 1, 1), picture="start.png")
        self.create_button(pos=(0, 0, -0.8), text='开始游戏', scale=0.15, parent=self.start_dialog, command=self.start, fg=(
            255/255, 220/255, 99/255, 1), frameColor=(147/255, 88/255, 51/255, 1))
        self.woodmens = []
        self.max_woodmen_num = 6
        self.spawn_time = 2
        self.spawnpoints = [Vec3(0, 210, 0), Vec3(-200, 220, 0), Vec3(-230, -210, 0), Vec3(-80, -190, 0),
                            Vec3(0, -200, 0), Vec3(-150, 20, 0), Vec3(0, -100, 0), Vec3(150, 20, 0)]

        self.wait_play_animation = []
        self.keep_play_animation = []
        self.end_dialog = self.create_dialog(frame_size=(-1.41,1.41,-1.01,1.01), pos = (0,0,0), color=(1,1,1,1), picture="win.png")
        self.end_dialog.hide()
        self.create_button(pos = (1.1,0,-0.8), text="退出游戏", scale=0.1, parent=self.end_dialog, command=self.quit, fg=(25/255, 22/255, 99/255, 1), frameColor = (247/255, 188/255, 51/255, 1))

    def window_properties(self, w, h):
        self.window = WindowProperties()
        self.window.setSize(w, h)
        self.win.requestProperties(self.window)

    def create_dialog(self, frame_size, pos, color, picture):
        return DirectDialog(frameSize=frame_size, frameColor=color,
                            pos=pos, frameTexture=picture)

    def create_button(self, text, parent, command, scale, pos, fg, frameColor):
        DirectButton(text=text, parent=parent, command=command, scale=scale,
                     pos=pos, text_font=self.font, text_fg=fg, frameColor=frameColor)

    def start(self):
        self.start_dialog.hide()
        self.load_model('FieldForest')
        base.cam.setHpr(-90, -4, 0)
        base.cam.setPos(-1000, -100, 100)
        self.create_fence(580, 350, 0, 580, -350, 0, 5)
        self.create_fence(-580, -350, 0, 580, -350, 0, 5)
        self.create_fence(-580, -350, 0, -580, -150, 0, 5)
        self.create_fence(-580, -40, 0, -580, 350, 0, 5)
        self.create_fence(-580, 350, 0, 580, 350, 0, 5)
        base.disableMouse()
        self.player = Player()
        self.friend = Friend(self)
        self.needle = EnemyNeedle()

        self.key_state = {'up': False, 'left': False,
                          'right': False, 'shoot': False}
        taskMgr.add(self.update)
        self.key_event()
        self.create_health_state()
        self.fog()

    def load_model(self, model):
        self.model = loader.loadModel(model)
        self.model.reparentTo(render)
        self.mina, self.minb = self.model.getTightBounds()
        return self.mina,self.minb

    def create_fence(self, ax, ay, az, bx, by, bz, r):
        fence_solid = CollisionCapsule(ax, ay, az, bx, by, bz, r)
        fence_node = CollisionNode('fence')
        fence_node.addSolid(fence_solid)
        render.attachNewNode(fence_node)
        mask = BitMask32()
        mask.setBit(0)
        mask.setBit(1)
        fence_node.setIntoCollideMask(mask)

    def change_key_state(self, direction, key_state):
        self.key_state[direction] = key_state

    def key_event(self):
        self.accept('w', self.change_key_state, ['up', True])
        self.accept('w-up', self.change_key_state, ['up', False])
        self.accept('d', self.change_key_state, ['right', True])
        self.accept('d-up', self.change_key_state, ['right', False])
        self.accept('a', self.change_key_state, ['left', True])
        self.accept('a-up', self.change_key_state, ['left', False])
        self.accept('woodmen-into-fence', self.change_woodmen_state)
        self.accept('mouse1', self.change_key_state, ['shoot', True])
        self.accept('mouse1-up', self.change_key_state, ['shoot', False])
        self.accept('woodmen-into-woodmen', self.change_woodmen_state)

    def update(self, task):
        if self.player.health > 0 and self.friend.health > 0:

            dt = globalClock.getDt()
            self.spawn_time -= dt
            if self.spawn_time <= 0:
                self.spawn_time = 2
                self.spawn_woodmen()

            [self.player.aduan_move(self.key_state, self.woodmen, dt)
            for self.woodmen in self.woodmens]
            [self.woodmen.woodmen_move(self.player,  dt, self.friend)
            for self.woodmen in self.woodmens]
            [self.friend.agency_judgement(
                self.player, dt, self.woodmen) for self.woodmen in self.woodmens]
            self.needle.attack(self.player, dt)

            self.aduan_health_bar['value'] = self.player.health
            self.aduan_health_bar['text'] = '生命值：'+str(self.player.health)
            self.friend_health_bar['value'] = self.friend.health
            self.friend_health_bar['text'] = '生命值：'+str(self.friend.health)
            self.woodmen_health_bar['value'] = self.player.transfer_woodmen_life
            self.woodmen_health_bar['text'] = '生命值：' + \
                str(self.player.transfer_woodmen_life)
            self.death_woodmens = [
                woodmen for woodmen in self.woodmens if woodmen.health < 0]
            [self.woodmens.remove(death_woodmen)
            for death_woodmen in self.death_woodmens]

            for death_woodmen in self.death_woodmens:
                death_woodmen.walking = False
                death_woodmen.collider.removeNode()
                death_woodmen.actor.disableBlend()
                death_woodmen.actor.play('die')
            self.keep_play_animation += self.death_woodmens

            for death_woodmen in self.keep_play_animation:
                if not death_woodmen.actor.getAnimControl('die').isPlaying():
                    death_woodmen.clean_up()
                    self.friend.count_health(5)
                    if self.friend.search_safe_house:
                        self.friend.walk_state = True
                else:
                    self.wait_play_animation.append(death_woodmen)
            self.keep_play_animation = self.wait_play_animation
            self.wait_play_animation = []
            if self.friend.success:
                self.end_dialog.show()
                self.health_dialog.hide()
        else:
            self.end_dialog["frameTexture"] = 'lose.png'
            self.end_dialog.show()
            self.health_dialog.hide()
        self.fog.update_fog(self.player.actor.getPos())

        return task.cont

    def change_woodmen_state(self, content):
        for self.woodmen in self.woodmens:
            if content.getFromNodePath() == self.woodmen.collider:
                self.woodmen.acceleration = -self.woodmen.acceleration
                self.woodmen.change_orientation = -self.woodmen.change_orientation

    def create_screen_image(self, image, pos, scale, parent):
        self.iamgeObject = OnscreenImage(
            image=image, pos=pos, scale=scale, parent=parent)
        self.iamgeObject.setTransparency(True)

    def create_health_bar(self, text, text_fg, text_scale, barColor, value, pos, scale, parent):
        return DirectWaitBar(text=text, text_fg=text_fg, text_scale=text_scale, text_font=self.font,
                             barColor=barColor, value=value, pos=pos, scale=scale, parent=parent)

    def create_health_state(self):
        self.health_dialog = self.create_dialog(frame_size=(
            0, 0, 0, 0), pos=(0, 0, 0), color=(0, 0, 0, 0), picture=None)
        self.create_screen_image(image='aduan_life.png', pos=(-1.13, 0, 0.88),
                                 scale=(0.24, 1, 0.09), parent=self.health_dialog)
        self.create_screen_image(image='codemao_life.png', pos=(-0.6, 0, 0.88),
                                 scale=(0.24, 1, 0.09), parent=self.health_dialog)
        self.create_screen_image(image='woodmen_life.png', pos=(
            1.1, 0, 0.88), scale=(0.24, 1, 0.09), parent=self.health_dialog)
        self.aduan_health_bar = self.create_health_bar(text='生命值：'+str(self.player.health),
                                                       text_fg=(1, 1, 0, 1), text_scale=(0.14, 0.14),
                                                       barColor=(1, 48/255, 48/255, 1), value=self.player.health,
                                                       pos=(-1.03, 0, 0.832), scale=(0.125, 1, 0.27),
                                                       parent=self.health_dialog)
        self.friend_health_bar = self.create_health_bar(text='生命值：'+str(self.friend.health),
                                                        text_fg=(1, 1, 0, 1), text_scale=(0.14, 0.14),
                                                        barColor=(1, 48/255, 48/255, 1), value=self.friend.health,
                                                        pos=(-0.5, 0, 0.832), scale=(0.125, 1, 0.27),
                                                        parent=self.health_dialog)
        self.woodmen_health_bar = self.create_health_bar(text='生命值：'+str(self.player.transfer_woodmen_life),
                                                         text_fg=(0, 178/255, 238/255, 1), text_scale=(0.14, 0.14),
                                                         barColor=(1, 0, 1, 1), value=self.player.transfer_woodmen_life,
                                                         pos=(1.2, 0, 0.842), scale=(0.125, 1, 0.27),
                                                         parent=self.health_dialog)

    def spawn_woodmen(self):
        if len(self.woodmens) < self.max_woodmen_num:
            self.woodmen = EnemyWoodmen(random.choice(self.spawnpoints))
            self.woodmens.append(self.woodmen)

    def input_box(self, scale, command, pos, parent):
        DirectEntry(scale=scale, command=command, pos=pos, parent=parent)

    def choose_dialog(self, text, text_fg, text_scale, pos, command, frameColor):
        return YesNoDialog(text_font=self.font, text=text, text_fg=text_fg,
                           text_scale=text_scale, pos=pos, command=command, frameColor=frameColor)
    
    def quit(self):
        self.player.clean_up()
        self.friend.clean_up()
        [self.woodmen.clean_up() for self.woodmen in self.woodmens]
        self.needle.clean_up()
        base.userExit()

    def fog(self):
        point_light = AmbientLight('ambient light')
        point_light.setColor((0.2,0.2,0.2,1))
        environment_light = render.attachNewNode(point_light)
        render.setLight(environment_light)
        self.fog = CreatFog(self.mina, self.minb)


if __name__ == '__main__':
    start_game = Config()
    start_game.run()
