from arcade import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
SCREEN_TITLE = 'My Fireworks'

FIREWORKS_INIT = 0
FIREWORKS_UP = 1
FIREWORKS_EXPLODE = 2
FIREWORKS_DIE = 3
FIREWORKS_COLORS = (color.GREEN, color.RED, color.SKY_BLUE, color.ORANGE)

FIREWORKS_EXPLODE_TIME = 2

class Firework():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = random.choice(FIREWORKS_COLORS)
        self.angle = random.randint(0, 360)
        self.v = random.randint(10, 30)
        self.max_y = SCREEN_HEIGHT - 200

    def draw(self):
        vx = self.v * math.sin(math.radians(self.angle))
        vy = self.v * math.cos(math.radians(self.angle))
        self.x += vx
        self.y += vy
        draw_point(self.x, self.y, self.color, self.size)


class Fireworks(Firework):
    def __init__(self, x, y, size, num):
        super().__init__(x, y, size)
        self.num = num
        self.setup()
    def setup(self):
        self.fireworks = []
        for i in range(self.num):
            firework = Firework(self.x, self.y, self.size)
            self.fireworks.append(firework)

    def draw(self):
        for firework in self.fireworks:
            firework.draw()


class MyFireworks(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        set_background_color(color.BLACK)
        self.status = FIREWORKS_INIT
        self.total_time = 0

    def on_draw(self):
        start_render()
        if self.status == FIREWORKS_UP:
            self.up_firework.draw()
        elif self.status == FIREWORKS_EXPLODE:
            self.explode_fireworks.draw()

    def create_up_fireworks(self):
        width, height = self.get_size()
        self.up_firework = Firework(width // 2,0,20)
        self.up_firework.max_y = height - 200
        self.up_firework.angle = 0
        self.up_firework.v = 5


    def create_explode_fireworks(self): 
        self.explode_fireworks = Fireworks(
            self.up_firework.x, self.up_firework.y, 5, 100)

    def on_key_release(self,symbol, modifiers):
        if self.status == FIREWORKS_INIT and symbol == key.SPACE:
            self.create_up_fireworks()
            self.status = FIREWORKS_UP
        elif symbol == key.F:
            self.set_fullscreen(True)
        elif symbol == key.Q:
            self.set_fullscreen(False)


    def on_update(self,delta_time):
        if self.status == FIREWORKS_UP:
            print("UP")
            if self.up_firework.y > self.up_firework.max_y:
                self.create_explode_fireworks()
                self.status = FIREWORKS_EXPLODE
        elif self.status == FIREWORKS_EXPLODE:
            self.total_time += delta_time
            print("Explode")
            if self.total_time > FIREWORKS_EXPLODE_TIME:
                self.status = FIREWORKS_DIE
                self.total_time = 0
        elif self.status== FIREWORKS_DIE:
            print("DIE")
            self.up_firework = None
            self.explode_fireworks = None
            self.status = FIREWORKS_INIT



if __name__ == '__main__':
    game = MyFireworks(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
    run()
