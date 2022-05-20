import arcade
import random

# 设置窗体宽和高
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 设置窗体标题
SCREEN_TITLE = "我的小车"


class MyDraw(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # 窗体初始化
        self.setup()
        self.balloons = []

    def setup(self):
        # 设置背景颜色
        arcade.set_background_color(arcade.color.WHITE)
        self.bx = 100
        self.by = 130
        self.bg_list = ['images/road.png', 'images/square.png']
        self.current_scene = 0
        self.change_bg()
    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        for balloon in self.balloons:
            balloon.draw()
        self.mydraw()

    def change_bg(self):
        self.bg = arcade.Sprite(self.bg_list[self.current_scene])
        self.bg.center_x = 400
        self.bg.center_y = 300

    def on_update(self,delta_time):
        self.bx += 5
        for balloon in self.balloons:
            balloon.center_y += 10
        if self.bx > SCREEN_WIDTH and self.current_scene == 0:
            self.bx = 100
            self.current_scene = 1
            self.change_bg()
            self.create_balloon()
        if self.bx > SCREEN_WIDTH and self.current_scene == 1:
            self.bx = 100
            self.current_scene = 0
            self.change_bg()
            balloons = []
        print(self.bx)

    def mydraw(self):
        # 车棚
        arcade.draw_rectangle_filled(self.bx, self.by + 70, 100, 80, arcade.color.RED)
        # 车窗
        arcade.draw_rectangle_filled(self.bx, self.by + 70, 40, 40, arcade.color.GRAY)
        # 车身
        arcade.draw_rectangle_filled(self.bx, self.by, 200, 60, arcade.color.RED)
        # 左轮
        arcade.draw_circle_filled(self.bx - 50, self.by - 30, 30, arcade.color.BLACK)
        # 右轮
        arcade.draw_circle_filled(self.bx + 50, self.by - 30, 30, arcade.color.BLACK)

    def create_balloon(self):
        balloon_list = ('images/balloon01.png',
                        'images/balloon02.png', 
                        'images/balloon03.png', 
                        'images/balloon04.png', 
                        'images/balloon05.png')
        num = 50
        for i in range(num):
            balloon = arcade.Sprite(random.choice(balloon_list))
            balloon.center_x = random.randint(0,SCREEN_WIDTH)
            balloon.center_y = -random.randint(300,600)
            self.balloons.append(balloon)


if __name__ == "__main__":
    game = MyDraw(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
