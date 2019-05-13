import pygame as pg

screen = pg.display.set_mode()

OBSTACLES = []
NODES = {}
NEIGHBORS = {}
RADIUS = 0

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_neighbors(self):
        return NEIGHBORS[self]
    def display(self):
        if self not in OBSTACLES:
            pg.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), RADIUS, 0)
        elif self in OBSTACLES:
            pg.draw.circle(screen, (100, 100, 100), (int(self.x), int(self.y)), RADIUS, 0)