import pygame as pg
import pathfinding as pf
import random

#initialize pygame module
pg.init()

#initialize screen variables
width = 600
height = 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("PathFinding")
clock = pg.time.Clock()
fps = 60

#initialize node values
pf.RADIUS = 6

#create each node
for Y in range(1, int(height/ (pf.RADIUS*2))):
    for X in range(1, int(width/ (pf.RADIUS*2))):
        x = X * pf.RADIUS*2
        y = Y * pf.RADIUS*2

        node = pf.Node(x, y)

        pf.NODES[(x, y)] = node
        if random.randint(0, 10) == 1:
            pf.OBSTACLES.append(node)

#set the neighbors for each node
for Y in range(1, int(height/ (pf.RADIUS*2))):
    for X in range(1, int(width/ (pf.RADIUS*2))):
        x = X * pf.RADIUS*2
        y = Y * pf.RADIUS*2

        neighbors = []

        if X > 1:
            neighbors.append(pf.NODES[(x - pf.RADIUS*2, y)])
        if Y > 1:
            neighbors.append(pf.NODES[(x, y - pf.RADIUS*2)])
        if X < int(width/ (pf.RADIUS*2))-1:
            neighbors.append(pf.NODES[(x + pf.RADIUS*2, y)])
        if Y < int(height/ (pf.RADIUS*2))-1:
            neighbors.append(pf.NODES[(x, y + pf.RADIUS*2)])

        pf.NEIGHBORS[pf.NODES[(x, y)]] = neighbors

#start loop
running = True
while running:
    #iterate through screen inputs
    for event in pg.event.get():
        #stop loop if screen exit
        if event.type == pg.QUIT:
            running = False

    #set background color
    screen.fill((0, 0, 0))

    for key in pf.NODES.keys():
        node = pf.NODES[key]
        node.display()

    #update screen variables
    pg.display.update()
    clock.tick(fps)