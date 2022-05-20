import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Hello World'

class MyDraw(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height,title)
        self.setup()
    def setup(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()
        self.mydraw()

    def mydraw(self):
        for y in range(25,600,50):
            arcade.draw_point(10,y,arcade.color.BLACK,20)
        for x in range(0,800,50):
            arcade.draw_point(x,10,arcade.color.BLACK,20)

        arcade.draw_line(50, 275, 50, 330, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(50, 325, 105, 325, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(100, 325, 100, 380, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(100, 375, 155, 375, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(150, 375, 150, 320, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(150, 325, 205, 325, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(200, 325, 200, 275, arcade.color.NEON_GREEN, 10)
        arcade.draw_line(205, 275, 45, 275, arcade.color.NEON_GREEN, 10)



if __name__ == '__main__':
    game = MyDraw(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()
