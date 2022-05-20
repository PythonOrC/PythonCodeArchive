import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "信件加密"


class PigPen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.images = arcade.SpriteList()
        self.count = 1

    def on_draw(self):
        arcade.start_render()
        self.images.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.BACKSPACE:
            if self.images:
                self.images.pop()
                self.count -= 1
        elif symbol == arcade.key.ENTER:
            screenshot = arcade.get_image(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            screenshot.save("screenshot.png", "PNG")
        elif len(self.images) < 50:
            image = arcade.Sprite("space.png")
            if 97 <= symbol <= 122:
                image = arcade.Sprite(f"{chr(symbol)}.png")
            image.left = (self.count - 1) * 100 % 1000
            image.top = (self.count - 1) // 10 * -100 + SCREEN_HEIGHT
            self.count += 1
            self.images.append(image)


if __name__ == "__main__":
    window = PigPen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
