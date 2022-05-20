from arcade import *

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_TITLE = 'My Rocket'


class Rocket():
    def __init__(self):
        self.flame_flag = True
        self.click_num = 0
        self.angle = 0
    def draw_rocket(self):
        ox, oy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ax, ay = ox, oy+100
        bx, by = ox, oy - 100 + self.click_num * 100
        cx, cy = bx - 45, by
        dx, dy = bx+45, by
        ex, ey = ax - 25, ay + 50
        fx, fy = ax + 25, ay + 50
        gx, gy = ax, ay + 100
        ljx, ljy = cx, cy - 50 - 5 - 40
        lkx, lky = bx, by - 50 - 5 - 50
        llx, lly = dx, dy - 50 - 5 - 40
        sjx, sjy = cx, cy - 50 - 5 - 30
        skx, sky = bx, by - 50 - 5 - 40
        slx, sly = dx, dy - 50 - 5 - 30
        if self.click_num <= 0:
            draw_rectangle_filled(cx, cy, 30, 100, color.COBALT)
            draw_rectangle_filled(bx, by, 50, 100, color.WHITE)
            draw_rectangle_filled(dx, dy, 30, 100, color.COBALT)
        if self.click_num <=1:
            draw_rectangle_filled(ox, oy, 30, 100, color.WHITE)
        if self.click_num <=2:
            draw_rectangle_filled(ax, ay, 50, 100, color.WHITE)
            draw_circle_outline(ax, ay, 10, color.COBALT, 5)
            draw_triangle_filled(ex, ey, fx, fy, gx, gy, color.RED)
            flame_color = color.TANGERINE
            if self.flame_flag:
                draw_rectangle_filled(ljx, ljy, 30, 80, flame_color)
                draw_rectangle_filled(lkx, lky, 30, 100, flame_color)
                draw_rectangle_filled(llx, lly, 30, 80, flame_color)
            else:
                draw_rectangle_filled(sjx, sjy, 30, 60, flame_color)
                draw_rectangle_filled(skx, sky, 30, 80, flame_color)
                draw_rectangle_filled(slx, sly, 30, 60, flame_color)
        if self.click_num >= 3:
            mx, my = ax, ay - 200
            draw_circle_filled(mx, my, 100, color.BLUE)
            R = 200
            sx,sy =mx + R * math.sin(math.radians(self.angle)), my + R * math.cos(math.radians(self.angle))
            draw_rectangle_filled(sx, sy, 50,100,color.WHITE, 180 - self.angle)
            draw_rectangle_filled(sx,sy,150,50,color.BLUE,180 - self.angle)
    def change_flame(self, time):
        self.flame_flag = not self.flame_flag


class MyRocket(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        set_background_color(color.SILVER)
        self.rocket = Rocket()
        schedule(self.rocket.change_flame, 0.3)

    def on_draw(self):
        start_render()
        self.rocket.draw_rocket()

    def on_mouse_release(self, x, y, button, modifiers):
            self.rocket.click_num += 1
    def on_update(self, delta_time):
        self.rocket.angle +=1


if __name__ == '__main__':
    game = MyRocket(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
