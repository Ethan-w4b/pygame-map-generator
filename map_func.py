import pygame as pg
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)
import json

# File path:  'C:/Users/Ethan/PycharmProjects/BC-T/Battle Cruiser Tact Files'

display_width = 600
display_height = 400



class SpriteSheet:
    def __init__(self,filename: str):
        # attempt to load sheet
        try:
            self.sheet = pg.image.load(f'assets/sheets/{filename}')
        except pg.error as e:
            print(f'Unable to load sheet image: {filename}')
            raise SystemExit(e)

        self.map = None

    def strip_from_sheet(self, sheet, start, size, columns, rows):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1+size[1]*j])
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames


def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames


def load_map(display, sheet, columns, rows):

    with open('MAP_DATA.json','r') as read_file:
        data = json.load(read_file)

    MAP = data['MAP1']
    target_y = 0
    target_x = 0
    x_pos = 0
    y_pos = 0
    pixel_width = rows*32-32

    for y in MAP:
        for x in MAP[0]:
            target_tile = MAP[target_y][target_x]
            display.blit(sheet[target_tile],(x_pos,y_pos))
            if target_x >= len(MAP[0])-1:
                target_x = 0
            else:
                target_x += 1

            if x_pos >= pixel_width:
                x_pos = 0
            else:
                x_pos += 32
        target_y += 1
        y_pos += 32


