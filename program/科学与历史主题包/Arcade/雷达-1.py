import arcade
import random
import math

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_TITLE = "My Radar"

RADAR_INIT = 0
RADAR_SEND = 1
RADAR_REFLEX = 2


class Target():
    def __init__(self):
        self.x, self.y = random.randint(
            0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)

    def draw(self):
        arcade.draw_point(self.x, self.y, arcade.color.RED, 20)


class Wave():
    def __init__(self, send_angle, reflex_x, reflex_y):
        self.send_angle = send_angle
        self.send_x, self.send_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.send_r = 0
        self.reflex_x, self.reflex_y = reflex_x, reflex_y
        self.reflex_r = 0

    def draw_send_wave(self):
        ox, oy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.send_x, self.send_y = ox + self.send_r * math.sin(math.radians(
            self.send_angle)), oy + self.send_r * math.cos(math.radians(self.send_angle))
        arcade.draw_point(self.send_x, self.send_y, arcade.color.BLACK, 10)
        self.send_r += 3

    def draw_reflex_wave(self):
        arcade.draw_circle_outline(self.reflex_x, self.reflex_y,
                            self.reflex_r, arcade.color.BLUE, 3)
        self.reflex_r += 3


class MyRadar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.angle = 0
        self.change_angle = 0
        self.target = Target()
        self.wave = Wave(self.angle, self.target.x, self.target.y)
        self.status = RADAR_INIT

    def on_draw(self):
        arcade.start_render()
        self.draw_radar()
        self.target.draw()
        if self.status == RADAR_SEND:
            self.wave.draw_send_wave()
        elif self.status == RADAR_REFLEX:
            self.wave.draw_reflex_wave()
        self.data()

    def on_update(self, delta_time):
        self.angle += self.change_angle
        if self.status == RADAR_SEND:
            if self.wave.send_x > SCREEN_WIDTH or self.wave.send_y > SCREEN_HEIGHT:
                self.status = RADAR_INIT
            self.dis = math.hypot(self.wave.send_x - self.target.x,
                                  self.wave.send_y - self.target.y)
            if self.dis <= 10:
                self.status = RADAR_REFLEX
        elif self.status == RADAR_REFLEX:
            dis = math.hypot(self.wave.send_x - SCREEN_WIDTH // 2,
                             self.wave.send_y - SCREEN_HEIGHT // 2)
            if self.wave.reflex_r >= dis:
                self.status = RADAR_INIT

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.change_angle = -1
        elif symbol == arcade.key.RIGHT:
            self.change_angle = 1

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.change_angle = 0
        if symbol == arcade.key.SPACE and self.status == RADAR_INIT:
            self.status = RADAR_SEND
            self.wave = Wave(self.angle, self.target.x, self.target.y)

    def draw_radar(self):
        ox, oy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ax, ay = ox - 25, oy - 80
        bx, by = ox, oy - 80
        cx, cy = ox + 25, oy - 80
        R = 50
        dx, dy = ox + R * math.sin(math.radians(self.angle)), oy + R * math.cos(math.radians(self.angle))
        arcade.draw_line(ox, oy, bx, by, arcade.color.BLACK, 5)
        arcade.draw_line(ax, ay, cx, cy, arcade.color.BLACK, 5)
        arcade.draw_ellipse_filled(ox, oy, 90, 32, arcade.color.BLACK, 180 - self.angle)
        arcade.draw_line(ox, oy, dx, dy, arcade.color.BLACK, 5)

    def data(self):
        if self.change_angle == -1:
            arcade.draw_text('向左转' + str(self.angle) + '度', 25, 50, arcade.color.BLACK,
                      font_name=('simhei'), font_size=20)
        elif self.change_angle == 1:
            arcade.draw_text('向右转' + str(self.angle * -1) + '度', 25, 50, arcade.color.BLACK,
                      font_name=('simhei'), font_size=20)
        else:
            arcade.draw_text('停转', 25, 50, arcade.color.BLACK,
                      font_name=('simhei'), font_size=20)
        # arcade.draw_text('距离' + str(round(self.dis,1)), 25, 25, arcade.color.BLACK,
                #   font_name=('simhei'), font_size=20)


if __name__ == '__main__':
    game = MyRadar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
