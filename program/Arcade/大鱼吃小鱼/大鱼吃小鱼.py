from arcade import *
from PIL import Image
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = '大鱼吃小鱼'
MOVEMENT_SPEED = 4
LEFT = 0
RIGHT = 1


class Player(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

        self.append_texture(load_texture(
            'resource/player.png', mirrored=True, scale=1))

        self.size = 2
        self.old_size = 2

    def update(self):
        super().update()

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        elif self.bottom < 0:
            self.bottom = 0

    def evolution(self, score):
        if score >= 16:
            self.size = 8
            self.scale = 1.5
        elif score >= 9:
            self.size = 6
            self.scale = 1.3
        elif score >= 4:
            self.size = 4
            self.scale = 1.2
        if self.size != self.old_size:
            print('Size: ' + str(int(self.size/2)))
            self.old_size = self.size


class Enemy(Sprite):
    def __init__(self, image):
        super().__init__(image)
        face = random.choice(['left', 'right'])
        speed = random.choice([1, 2, 3, 4, 5])
        if face == 'left':
            self.center_x = SCREEN_WIDTH + 60
            self.change_x = -speed
        else:
            self.center_x = -60
            self.append_texture(load_texture(image, mirrored=True, scale=1))
            self.set_texture(RIGHT)
            self.change_x = speed
        self.center_y = random.randint(0, SCREEN_HEIGHT)


class Status(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT//2

class PowerUps(Sprite):
    def __init__(self, image):
        super().__init__(image)
        speed = random.choice([1, 2, 3, 4, 5])
        self.center_y = SCREEN_HEIGHT + 50
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.change_y = -speed

class MyGame(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        Image.open('resource/sea.png').resize((SCREEN_WIDTH,
                                               SCREEN_HEIGHT)).save('resource/new_sea.png')
        self.background = Sprite('resource/new_sea.png')
        self.background.center_x = SCREEN_WIDTH // 2
        self.background.center_y = SCREEN_HEIGHT // 2
        self.player_sprite = Player('resource/player.png')
        self.player_sprite_list = SpriteList()
        self.player_sprite_list.append(self.player_sprite)
        self.fishes = {'resource/黄鱼.png': (1,1),
                       'resource/绿鱼.png': (3,2), 'resource/红鱼.png': (5,3), 'resource/紫鱼.png': (7,4), 'resource/蓝鱼.png': (9,5)}
        self.enemy_sprite_list = SpriteList()
        self.hearts = PowerUps('resource/心.png')
        self.total_time = 0
        self.last_time = 0
        self.create_num = 1
        self.target_num = 0
        self.enemy_num = 0
        self.score = 0
        self.old_score = 0
        self.game_over_status = False
        self.pause_game_status = False
        self.game_over = Status('resource/game_over.png')
        self.pause_game = Status('resource/game_pause.png')
        self.eat_sound = load_sound('resource/eat_sound.wav')
        self.game_over_sound = load_sound('resource/game_over_sound.wav')

    def on_draw(self):
        start_render()
        self.background.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        if int(self.total_time) % 5 == 0:
            self.show = random.choices([True,False],(0.6,0,4))[0]
            if self.show:
                self.hearts.draw()
                print('powerup')
        self.data()
        if self.game_over_status:
            self.game_over.draw()
            if int(self.total_time)%2 == 0:
                draw_text('Press "Tab" to restart', start_x=SCREEN_WIDTH//2 - 145, start_y=100, color=color.WHITE,
                        font_name=('simhei'), font_size=20)
        if self.pause_game_status:
            self.pause_game.draw()

    def on_update(self, delta_time):
        self.total_time += delta_time
        if not self.game_over_status and not self.pause_game_status:
            if int(self.total_time) != int(self.last_time) and int(self.total_time) % 30 == 0:
                self.create_num += 1

            if int(self.total_time) % 1 == 0 and int(self.last_time) != int(self.total_time):
                self.create_enemy()
                self.last_time = self.total_time
            if self.create_num != self.target_num:
                print('Target Enemy Fish: ' + str(self.create_num))
                self.target_num = self.create_num
            self.player_sprite_list.update()
            self.enemy_sprite_list.update()

            for enemy in self.enemy_sprite_list:
                if enemy.center_x < -60 or enemy.center_x > SCREEN_WIDTH + 60:
                    enemy.kill()
            if len(self.enemy_sprite_list) != self.enemy_num:
                print('Fish On Screen: ' + str(len(self.enemy_sprite_list)))
                self.enemy_num = len(self.enemy_sprite_list)
            hit_list = check_for_collision_with_list(
                self.player_sprite, self.enemy_sprite_list)
            if hit_list:
                for hit in hit_list:
                    if self.player_sprite.size > hit.size:
                        hit.kill()
                        play_sound(self.eat_sound)
                        self.score += hit.score
                    else:
                        self.player_sprite.kill()
                        play_sound(self.game_over_sound)
                        self.game_over_status = True
            self.player_sprite.evolution(self.score)
            if self.score != self.old_score:
                print('Score: ' + str(self.score) + ' fish')
                self.old_score = self.score

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif symbol == key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif symbol == key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            self.player_sprite.set_texture(LEFT)
        elif symbol == key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_sprite.set_texture(RIGHT)
        elif symbol == key.RETURN:
            image = get_image(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            image.save('screenshot.png')
        elif symbol == key.ESCAPE and self.game_over_status == False:
            self.pause_game_status = not self.pause_game_status
        elif symbol == key.TAB and self.game_over_status == True:
            self.setup()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP or symbol == key.DOWN:
            self.player_sprite.change_y = 0
        elif symbol == key.LEFT or symbol == key.RIGHT:
            self.player_sprite.change_x = 0

    def create_enemy(self):
        for i in range(self.create_num):
            fish = random.choices(list(self.fishes.keys()),[0.1,0.15,0.75,0.75,0.5])[0]
            enemy_sprite = Enemy(fish)
            enemy_sprite.size = self.fishes[fish][0]
            enemy_sprite.score = self.fishes[fish][1]
            self.enemy_sprite_list.append(enemy_sprite)

    def data(self):

        draw_text('Fish On Screen: ' + str(len(self.enemy_sprite_list)), 10, 35,
                  color.BLUE, font_name=('simhei'), font_size=20)
        draw_text('Level: ' + str(self.create_num) + ' fish', 10, 10,
                  color.BLUE, font_name=('simhei'), font_size=20)
        draw_text('Score: ' + str(self.score) + ' fish', 10, 60,
                  color.BLUE, font_name=('simhei'), font_size=20)
        draw_text('Size: ' + str(int(self.player_sprite.size/2)), 10, 85,
                  color.BLUE, font_name=('simhei'), font_size=20)


if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
