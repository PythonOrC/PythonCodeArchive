import arcade
import math
import datetime


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

SCREEN_TITLE = "My Clock"

CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2


class Pointer():
    def __init__(self, name, value, length, color, line_width):
        self.name = name
        self.value = value
        self.length = length
        self.color = color
        self.line_width = line_width

    def draw(self):
        if self.name == 'hour':
            angle = 360 * self.value / 12
        else:
            angle = 360 * self.value / 60
        x, y = CENTER_X + self.length * \
            math.sin(math.radians(angle)), CENTER_Y + \
            self.length * math.cos(math.radians(angle))
        arcade.draw_line(CENTER_X, CENTER_Y, x, y, self.color, self.line_width)


class MyClock(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.mydraw()

    def mydraw(self):
        r = 200
        arcade.draw_circle_outline(
            CENTER_X, CENTER_Y, r, arcade.color.SKY_BLUE, 20)
        per = 360/12
        for i in range(1, 13):
            angle = per * i
            x, y = CENTER_X + (r-20) * math.sin(math.radians(angle)
                                                ), CENTER_Y + (r-20) * math.cos(math.radians(angle))
            arcade.draw_text(str(i), x, y, arcade.color.BLACK, 20, font_name=(
                'simhei'), anchor_x="center", anchor_y="center")
        import datetime
        d = datetime.datetime.now()
        h, m, s = d.hour, d.minute, d.second
        hour = Pointer('hour', h, 70, arcade.color.GREEN, 15)
        minute = Pointer('minute', m, 120, arcade.color.BLUE, 10)
        second = Pointer('second', s, 150, arcade.color.RED, 5)
        hour.draw()
        minute.draw()
        second.draw()
        arcade.draw_circle_filled(CENTER_X, CENTER_Y, 10, arcade.color.BLACK)
        year, month, day, week = d.year, d.month, d.day, d.weekday()
        weeks = ['一', '二', '三', '四', '五', '六', '天']
        date = f"{year}年{month}月{day}日 星期{weeks[week]}"
        arcade.draw_text(date, CENTER_X, CENTER_Y - 250, arcade.color.BLACK,
                         20, font_name=('simhei'), anchor_x='center', anchor_y='center')


if __name__ == '__main__':
    game = MyClock(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
