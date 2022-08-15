import pygame as pg
from map_func import strip_from_sheet
import sys
import random
import json



DISPLAY_HEIGHT = 400
DISPLAY_WIDTH = 600
FPS = 30




'''def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames'''

def load_map(sheet):
    with open('MAP_DATA.json','r') as r_file:
        file_data = json.load(r_file)

    MAP = file_data['MAP1']
    target_y = 0
    target_x = 0
    y_pos = 0
    x_pos = 0

    for y in MAP:
        for x in MAP[0]:
            #print(f'x is {target_x}, y is {target_y}')
            #print(f'x is {x_pos}, y is {y_pos}')
            target_tile = MAP[target_y][target_x]
            gameDisplay.blit(sheet[target_tile],(x_pos,y_pos))
            if target_x >= len(MAP[0])-1:
                target_x = 0
            else:
                target_x += 1

            if x_pos >= 480:
                x_pos = 0
            else:
                x_pos += 32
        target_y += 1
        y_pos += 32





def mouse_over_map():
    mx,my = pg.mouse.get_pos()
    return mx,my


tile_sheet = pg.image.load('assets/sheets/tileset.png')
test_sheet = strip_from_sheet(tile_sheet, (0,0), (32,32), 6, 4)

menu_btn_img = pg.image.load('assets/Sprites/menu-sprites/menu-frame-v2.png')
menu_btn_img = pg.transform.scale(menu_btn_img, (64,64))



class Player:
    def __init__(self,img,initial_pos):
        self.img = img
        self.rect = img.get_rect(topleft=initial_pos)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update_sprite(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_w]:
            self.move(0, -3)
        if pressed_key[pg.K_s]:
            self.move(0, 3)
        if pressed_key[pg.K_a]:
            self.move(-3, 0)
        if pressed_key[pg.K_d]:
            self.move(3, 0)

        # border control
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.rect.bottom = DISPLAY_HEIGHT



    def draw(self, surface):
        surface.blit(self.img, self.rect)






player_sprite = pg.image.load('assets/Sprites/player_sprite.png')
player_sprite = pg.transform.scale(player_sprite, (34,34))

player1 = Player(player_sprite, (10,10))

click = False




def mainLoop():
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print('Jump!')


        gameDisplay.fill((0, 0, 0))
        load_map(test_sheet)
        player1.update_sprite()
        player1.draw(gameDisplay)
        pg.display.update()
        clock.tick(FPS)


pg.init()

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
mainLoop()
