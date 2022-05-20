import arcade
import math

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

SCREEN_TITLE = "雷达扫描动画"


class MyScan(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.angle = 0

    def on_draw(self):
        arcade.start_render()
        self.mydraw()

    def mydraw(self):
        oy, ox = SCREEN_HEIGHT//2, SCREEN_WIDTH // 2
        arcade.draw_circle_filled(ox, oy, 220, arcade.color.LIGHT_SKY_BLUE)
        arcade.draw_circle_filled(ox, oy, 200, arcade.color.ROYAL_BLUE)
        r = 200
        for i in range(1, 4):
            arcade.draw_circle_outline(ox, oy, 50 * i, arcade.color.LIGHT_SKY_BLUE, 5)

        for i in range(4):
            angle = 45 * i
            start_x, start_y = ox + r * \
                math.sin(math.radians(angle)), oy + r * \
                math.cos(math.radians(angle))
            end_x, end_y = ox + r * \
                math.sin(math.radians(angle + 180)), oy + r * \
                math.cos(math.radians(angle + 180))
            arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.LIGHT_SKY_BLUE, 5)
        for i in range(30):
            sx, sy = ox + r * \
                math.sin(math.radians(self.angle + i)), oy + r * \
                math.cos(math.radians(self.angle + i))
            arcade.draw_line(ox, oy, sx, sy, arcade.color.LIGHT_SKY_BLUE, 5)
        arcade.draw_arc_outline(ox, oy, r + 10, r + 10, arcade.color.RED, 60 - self.angle, 90, 20)

    def on_update(self, delta_time):
        self.angle += 3
        if self.angle + 30 >= 360:
            self.angle = 0


if __name__ == '__main__':
    game = MyScan(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
