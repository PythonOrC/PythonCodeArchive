import pygame

pygame.init()
screen = pygame.display.set_mode([800, 800])

keep_going = True
pic_right = pygame.image.load('1.png')
pic_left = pygame.image.load('1.png')
pic = pic_right
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speedx
    picy += speedy
    if picx <= 0:
        speedx = -speedx
        pic = pic_right
    if picx + pic.get_width() >= 800:
        speedx = -speedx
        pic = pic_left
    if picy <= 0 or picy + pic.get_height() >= 800:
        speedy = -speedy
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()
