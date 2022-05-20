from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from player import *
from friend import *
from enemy import *

class Config(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.font = loader.loadFont('font.ttc')
        self.setup()

    def setup(self):
        self.window_properties(1400, 1000)
        self.start_dialog = self.create_dialog(
            frame_size=(-1.41, 1.41, -1.01, 1.01), pos=(0, 0, 0), color=(1, 1, 1, 1), picture="start.png")
        self.create_button(pos=(0, 0, -0.8), text='开始游戏', scale=0.15, parent=self.start_dialog, command=self.start, fg=(
            255/255, 220/255, 99/255, 1), frameColor=(147/255, 88/255, 51/255, 1))

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
        self.friend = Friend()
        self.woomen = EnemyWoodmen()
        self.needle = EnemyNeedle()
        

    def load_model(self, model):
        self.model = loader.loadModel(model)
        self.model.reparentTo(render)

    def create_fence(self, ax, ay, az, bx, by, bz, r):
        fence_solid = CollisionCapsule(ax, ay, az, bx, by, bz, r)
        fence_node = CollisionNode('fence')
        fence_node.addSolid(fence_solid)
        render.attachNewNode(fence_node)


if __name__ == '__main__':
    start_game = Config()
    start_game.run()
