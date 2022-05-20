from arcade import *
from math import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

SCREEN_TITLE = "彩虹"


class MyScan(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        set_background_color(color.WHITE)
        self.color = [color.RED, color.ORANGE, color.YELLOW,
                      color.LIGHT_GREEN, color.BLUE, color.PURPLE, color.MAGENTA]

    def on_draw(self):
        start_render()
        self.mydraw()

    def mydraw(self):
        oy, ox = SCREEN_HEIGHT//2, SCREEN_WIDTH // 2
        r = 200
        for i in range(6):
            draw_arc_outline(ox, oy, r + 10 * i, r + 10 * i, self.color[i],
                             0, 180, 10)


if __name__ == '__main__':
    game = MyScan(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
