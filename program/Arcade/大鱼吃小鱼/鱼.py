from arcade import *
from PIL import Image
import random

# 设置窗体宽和高
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
# 设置窗体标题
SCREEN_TITLE = "大鱼吃小鱼"
#存储玩家角色每次移动的速度
MOVEMENT_SPEED = 4
LEFT = 0  # 角色向左的造型索引
RIGHT = 1  # 角色向右的造型索引

class Prop(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT + 30
        self.change_y = -4

class Player(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

        self.append_texture(load_texture(
            "resource/player.png", mirrored=True, scale=1))
        self.size = 2

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
    #进化
    def evolution(self, score):
        if score >= 3:
            self.size = 8
            self.scale = 1.5
        elif score >= 2:
            self.size = 6
            self.scale = 1.3
        elif score >= 1:
            self.size = 4
            self.scale = 1.2

class Enemy(Sprite):
    def __init__(self, image):
        super().__init__(image)
        #随机选择敌人的生成位置
        face = random.choice(["left", "right"])
        #随机选择敌人的移动速度
        speed = random.choice([1, 2, 3, 4, 5])
        if face == "left":
            self.center_x = SCREEN_WIDTH + 60
            self.change_x = -speed
        elif face == "right":
            self.center_x = -60
            #设置敌人的向右造型
            self.append_texture((load_texture(image, mirrored=True, scale=1)))
            self.set_texture(RIGHT)
            self.change_x = speed
        self.center_y = random.randint(0, SCREEN_HEIGHT)

class Status(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT //2

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #窗口初始化
        self.setup()

    def setup(self):
        self.prop_list = SpriteList()
        #上一次试图创建道具的时刻
        self.last_prop_time = 0
        #用pillow 调整背景图片大小以适配窗体宽高
        Image.open("resource/sea.png").resize((SCREEN_WIDTH,
                                               SCREEN_HEIGHT)).save("resource/new_sea.png")
        #设置背景图片
        self.background = Sprite("resource/new_sea.png")
        self.background.center_x = SCREEN_WIDTH // 2
        self.background.center_y = SCREEN_HEIGHT // 2
        #添加玩家角色
        self.player_sprite = Player("resource/player.png")
        self.player_sprite_list = SpriteList()
        self.player_sprite_list.append(self.player_sprite)
        #添加电脑角色
        self.fishes = {"resource/黄鱼.png": (1,1), "resource/绿鱼.png": (3,2),
                       "resource/红鱼.png": (5,3), "resource/紫鱼.png": (7,4), "resource/蓝鱼.png": (9,5)}
        self.enemy_sprite_list = SpriteList()
        self.total_time = 0
        self.last_time = 0
        #存储每次要生成敌人的数量
        self.create_num = 1
        self.score = 0
        self.game_over_status = False # 判断游戏是否结束
        self.game_over = Status("resource/game_over.png")
        self.game_pause_status = False  # 判断游戏是否暂停
        self.game_pause = Status("resource/game_pause.png")

        self.eat_sound = load_sound("resource/eat_sound.wav")
        self.game_over_sound = load_sound("resource/game_over_sound.wav")
        
    def on_draw(self):
        start_render()
        self.background.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        self.prop_list.draw()
        #显示分数
        draw_text(f"score:{self.score}", 0, SCREEN_HEIGHT-20,
                  color.WHITE, font_name=("simhei", "PingFang"), font_size=20)
        
        #游戏结束提示
        if self.game_over_status:
            self.game_over.draw()
            if int(self.total_time)% 2 == 0:
                draw_text("请按下 TAB 键重新开始游戏",start_x=300,start_y=100,color=color.WHITE,font_name=("simhei","PingFang"),font_size=20)
        
        #游戏暂停提示
        if self.game_pause_status:
            self.game_pause.draw()
      
    def on_update(self, delta_time):
        #每隔5秒试图创建道具，也需要考虑当前时刻与上一次试图创建道具的时刻不相同
        if int(self.total_time) != int(self.last_prop_time) and int(self.total_time) % 5 == 0:
            #根据设置的概率创建道具
            #每5秒有百分之10的概率会创建道具
            if random.choices([True, False], [0.1, 0.9])[0]:
                prop = Prop("resource/心.png")
                self.prop_list.append(prop)
                self.last_prop_time = self.total_time

            #玩家角色与道具的碰撞检测
        hit_list = check_for_collision_with_list(self.player_sprite, self.prop_list)
        for hit in hit_list:
            hit.kill()  # 碰撞的道具移出精灵组
            self.score += 10
        self.prop_list.update()

        self.total_time += delta_time
        if self.game_over_status or self.game_pause_status:
            return
        
        #总时间到某个点后提高生成速度
        if int(self.total_time) != int(self.last_time) and int(self.total_time) % 300 == 0:
            self.create_num += 1
        #每隔1秒创建敌人
        if int(self.total_time) != int(self.last_time) and int(self.total_time) % 1 == 0:

            self.create_enemy()
            self.last_time = self.total_time

        self.player_sprite_list.update()
        self.enemy_sprite_list.update()

        for enemy in self.enemy_sprite_list:
            if enemy.center_x < -60 or enemy.center_x > SCREEN_WIDTH + 60:
                enemy.kill()

        #玩家角色与电脑角色的碰撞检测
        hit_list = check_for_collision_with_list(
            self.player_sprite, self.enemy_sprite_list)
        if hit_list:
            for hit in hit_list:
                if self.player_sprite.size > hit.size:
                    play_sound(self.eat_sound)
                    hit.kill()
                    self.score += hit.score
                else:
                    self.player_sprite.kill()
                    play_sound(self.game_over_sound)
                    self.game_over_status = True

        self.player_sprite.evolution(self.score)

    def on_key_press(self, symbol, modifiers):  # 按下某个键时触发
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
        elif symbol == key.RETURN:  # 按回车截图
            image = get_image(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            image.save('screenshot.png')
        elif symbol == key.ESCAPE:
            self.game_pause_status = not self.game_pause_status
        elif symbol == key.TAB:
            if self.game_over_status:
                self.setup()
              
    def on_key_release(self, symbol, modifiers):  # 松开某个键时触发
        if symbol == key.UP or symbol == key.DOWN:
            self.player_sprite.change_y = 0
        elif symbol == key.LEFT or symbol == key.RIGHT:
            self.player_sprite.change_x = 0

    #创建敌人的方法
    def create_enemy(self):
        for i in range(self.create_num):
            #随机选择敌人的图片素材
            fish = random.choices(list(self.fishes.keys()),[0.3, 0.1, 0.05, 0.05, 0.5])[0]
            enemy_sprite = Enemy(fish)
            enemy_sprite.size = self.fishes[fish][0]
            enemy_sprite.score = self.fishes[fish][1]
            self.enemy_sprite_list.append(enemy_sprite)
            
if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()