from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *


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


if __name__ == '__main__':
    start_game = Config()
    start_game.run()
