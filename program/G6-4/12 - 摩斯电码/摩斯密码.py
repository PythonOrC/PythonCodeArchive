import json
import arcade

SCREEN_HEIGHT = 200
SCREEN_WIDTH = 300
SCREEN_TITLE = "摩斯密码"


class Morse(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.char = " "
        self.code = " "
        self.di = arcade.load_sound("di.wav")
        self.do = arcade.load_sound("do.wav")
        with open("morse.json", "r") as f:
            self.morse = json.load(f)

    def on_draw(self):
        arcade.start_render()
        x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        arcade.draw_text(
            self.char, x, y, arcade.color.BLUE, 20, anchor_x="center", anchor_y="bottom"
        )
        arcade.draw_text(
            self.code, x, y, arcade.color.RED, 20, anchor_x="center", anchor_y="top"
        )

    def on_key_press(self, event, modifer):
        if event <= 65535:
            if chr(event).upper() in self.morse.keys():
                self.char = chr(event).upper()
                self.code = self.morse[chr(event).upper()]

            for i in self.code:
                if i == ".":
                    self.di.play()
                else:
                    self.do.play()
                arcade.pause(0.3)


if __name__ == "__main__":
    m = Morse(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
