import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 730
SCREEN_TITLE = "遮罩解码"
MOVEMENT_SPEED = 1


class Decrypt(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        self.background = arcade.Sprite("信.png")
        self.background.center_x = self.background.width // 2
        self.background.center_y = self.background.height // 2
        self.tool = arcade.Sprite("密码卡.png")
        self.tool.center_x = self.tool.width // 2
        self.tool.center_y = self.tool.height // 2

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.tool.draw()

    def on_update(self, delta_time):
        self.tool.update()

    def on_key_press(self, event, modifier):
        if event == arcade.key.UP:
            self.tool.change_y = MOVEMENT_SPEED
        elif event == arcade.key.DOWN:
            self.tool.change_y = -MOVEMENT_SPEED
        elif event == arcade.key.LEFT:
            self.tool.change_x = -MOVEMENT_SPEED
        elif event == arcade.key.RIGHT:
            self.tool.change_x = MOVEMENT_SPEED

    def on_key_release(self, event, modifier):
        if event == arcade.key.UP or event == arcade.key.DOWN:
            self.tool.change_y = 0
        elif event == arcade.key.LEFT or event == arcade.key.RIGHT:
            self.tool.change_x = 0


if __name__ == "__main__":
    window = Decrypt(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
