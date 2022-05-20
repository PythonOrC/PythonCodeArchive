from arcade import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_TITLE = "雪花"


class SnowFlakes(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        set_background_color(color.WHITE)
        self.angle = 0

    def on_draw(self):
        start_render()
        self.draw_snowflakes()


    def draw_snowflakes(self):
        ox, oy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        for i in range(4):
            draw_ellipse_filled(ox, oy, 200,400,color.SKY_BLUE, 180 - self.angle)
            self.angle += 45



if __name__ == '__main__':
    game = SnowFlakes(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
