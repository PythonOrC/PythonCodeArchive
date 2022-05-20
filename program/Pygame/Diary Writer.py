import pygame as pg
import datetime
date = datetime.datetime.now()

def main():
    screen = pg.display.set_mode((600, 600))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(10, 300, 150, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue1')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    keys = pg.key.get_pressed()
                    if keys[pg.K_LCTRL] and keys[pg.K_RETURN]:
                        print(text)
                        with open('Diary.txt','a+') as f:
                            f.write(str(date)+'\n\n')
                            f.write(text+'\n\n\n')
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()

