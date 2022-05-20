from arcade import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = '我的小车'


class MyDraw(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        set_background_color(color.WHITE)

    def on_draw(self):
        start_render()
        self.mydraw()

    def mydraw(self):
        bx, by = 400,300
        draw_rectangle_filled(bx,by+70,100,80,color.RED)
        draw_rectangle_filled(bx,by+70,40,40,color.GRAY)
        draw_rectangle_filled(bx,by, 200, 60, color.RED)
        draw_circle_filled(bx-50, by-30,30,color.BLACK)
        draw_circle_filled(bx+50, by-30, 30, color.BLACK)
        draw_text('--by 胡弘毅',bx+100,by-30-50,color.BLUE, font_name = ('simhei'))
if __name__ == '__main__':
    game = MyDraw(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
