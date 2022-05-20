import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((228, 512))
background = pygame.image.load('assets/background.png')
bgm = pygame.mixer.Sound('sound/bgm.wav')
fly = pygame.mixer.Sound('sound/fly.wav')
pygame.mixer.Channel(1).play(bgm)

pygame.display.set_caption('Flappy Bird')
playing = True
clock = pygame.time.Clock()


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.birdSprites = [
            pygame.image.load('assets/0.png'), 
            pygame.image.load('assets/1.png'), 
            pygame.image.load('assets/2.png')
        ]
        self.birdSprite = self.birdSprites[0]
        self.x = 50
        self.y = 100
        self.flapSpeed = 7
        self.gravity = 0.4
        self.rect = self.birdSprite.get_rect()
        self.rect.topleft = (self.x, self.y)

    def birdUpdate(self):
        self.flapSpeed -= self.gravity
        self.y -= self.flapSpeed
        self.rect.topleft = (self.x, self.y)
        if self.flapSpeed < 0:
            self.birdSprite = self.birdSprites[1]
        elif self.flapSpeed > 0:
            self.birdSprite = self.birdSprites[2]
        else:
            self.birdSprite = self.birdSprites[0]

    def birdCollide(self):
        global playing
        collisionTop = self.rect.colliderect(pipe.topRect)
        collisionBottom = self.rect.colliderect(pipe.bottomRect)
        if collisionTop or collisionBottom or self.y > 512-120:
            hit = pygame.mixer.Sound('sound/hit.wav')
            pygame.mixer.Channel(3).play(hit)
            time.sleep(0.5)
            print(collisionTop, collisionBottom, pipe.bottomRect, self.rect)
            playing = False
            


class Pipe:
    def __init__(self):
        self.bottom = pygame.image.load('assets/bottom.png')
        self.top = pygame.image.load('assets/top.png')
        self.gap = 50
        self.x = 288
        self.yOffset = random.randint(70, 170)
        self.topRect = self.top.get_rect()
        self.bottomRect = self.bottom.get_rect()
        self.topY = 0 - self.gap - self.yOffset 
        self.bottomY = 360 + self.gap - self.yOffset
        
        self.topRect.topleft = (self.x, self.topY)
        self.bottomRect.topleft = (self.x, self.bottomY)

    def pipeUpdate(self):
        self.x -= 2
        self.topRect.topleft = (self.x, self.topY)
        self.bottomRect.topleft = (self.x, self.bottomY)
        if self.x < -80:
            self.x = 288
            self.yOffset = random.randint(70, 170)
            self.topY = 0 - self.gap - self.yOffset
            self.bottomY = 360 + self.gap - self.yOffset
        
class Ground():
    def __init__(self,x):
        self.x = -10+x
        self.y = 512-120
        self.groundSprite = pygame.image.load('assets/ground.png')
    
    def groundUpdate(self):
        self.x -= 2
        if self.x < -288:
            self.x = 288



bird = Bird()
pipe = Pipe()
ground1 = Ground(0)
ground2 = Ground(288)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flapSpeed = 7
            pygame.mixer.Channel(2).play(fly)
    screen.blit(background, (0, 0))
    screen.blit(bird.birdSprite, (bird.x, bird.y))
    screen.blit(pipe.bottom, (pipe.x, pipe.bottomY))
    screen.blit(pipe.top, (pipe.x, pipe.topY))
    screen.blit(ground1.groundSprite, (ground1.x, ground1.y))
    screen.blit(ground2.groundSprite, (ground2.x, ground2.y))
    bird.birdUpdate()
    pipe.pipeUpdate()
    bird.birdCollide()
    ground1.groundUpdate()
    ground2.groundUpdate()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
