class intCodeComp(object):
    def __init__(self, code):
        self.code = code[:]
        for _ in range(0,20000):
            self.code.append(0)
        self.inputs = []
        self.outputs = []
        self.relBase = 0
        self.halt = False
        self.awaitInput = False
        self.i = 0
    def run(self):
        i = self.i
        inv = 0
        outs = []
        while i < len(self.code):
            ip = str(self.code[i])[0:-2]
            ip = (("0" * (3 - len(ip))) + ip)[::-1]
            opc = int(str(self.code[i])[::-1][0:2][::-1])
            #print(i, opc, ip)
            if opc == 1:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                l3 = self.code[i + 3] + self.relBase if ip[2] == "2" else self.code[i + 3]
                self.code[l3] = self.code[l1] + self.code[l2]
                i += 4
            elif opc == 2:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                l3 = self.code[i + 3] + self.relBase if ip[2] == "2" else self.code[i + 3]
                self.code[l3] = self.code[l1] * self.code[l2]
                i += 4
            elif opc == 3:
                if inv == len(self.inputs):
                    self.i = i
                    self.awaitInput = True
                    return
                self.awaitInput = False
                l1 = self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1]
                self.code[l1] = int(self.inputs[inv])
                inv += 1
                i += 2
            elif opc == 4:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                self.outputs.append(self.code[l1])
                i += 2
            elif opc == 5:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                if self.code[l1] != 0:
                    i = self.code[l2]
                else:
                    i += 3
            elif opc == 6:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                if not self.code[l1] != 0:
                    i = self.code[l2]
                else:
                    i += 3
            elif opc == 7:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                l3 = self.code[i + 3] + self.relBase if ip[2] == "2" else self.code[i + 3]
                if self.code[l1] < self.code[l2]:
                    self.code[l3] = 1
                else:
                    self.code[l3] = 0
                i += 4
            elif opc == 8:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                l2 = i + 2 if ip[1] == "1" else (self.code[i + 2] + self.relBase if ip[1] == "2" else self.code[i + 2])
                l3 = self.code[i + 3] + self.relBase if ip[2] == "2" else self.code[i + 3]
                if self.code[l1] == self.code[l2]:
                    self.code[l3] = 1
                else:
                    self.code[l3] = 0
                i += 4
            elif opc == 9:
                l1 = i + 1 if ip[0] == "1" else (self.code[i + 1] + self.relBase if ip[0] == "2" else self.code[i + 1])
                self.relBase += self.code[l1]
                i += 2
            elif self.code[i] == 99:
                self.halt = True
                return
            else:
                print("... unknown op code")
                self.halt = True
                return
    def readOutputs(self):
        tmp = self.outputs
        self.outputs = []
        return tmp
    def setInputs(self, *inputs):
        self.inputs = inputs

a = [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,101,0,1034,1039,101,0,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,101,0,1034,1039,102,1,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,1001,1037,0,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1001,1035,0,1040,1001,1038,0,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,7,1032,1006,1032,165,1008,1040,5,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,0,1,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,27,1044,1106,0,224,1102,1,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,101,0,1040,1035,102,1,1041,1036,1001,1043,0,1038,102,1,1042,1037,4,1044,1106,0,0,13,3,18,86,2,10,5,16,95,16,54,4,23,63,70,10,21,20,26,99,85,9,96,3,83,5,9,91,14,1,4,78,11,15,53,10,35,13,7,17,30,90,23,65,65,67,16,4,65,39,11,57,13,36,22,95,53,63,22,47,12,47,2,12,3,71,92,17,55,16,51,79,6,3,92,15,17,15,18,63,8,12,3,49,6,69,32,1,25,83,17,12,1,76,23,95,17,13,92,13,56,16,69,94,11,20,31,83,30,21,88,22,61,45,6,70,12,3,30,23,86,6,93,4,24,9,73,72,7,72,83,9,30,6,24,86,99,11,11,96,16,68,10,35,19,23,6,79,51,8,3,8,75,2,32,26,73,23,80,30,86,25,64,46,24,81,20,18,85,7,94,28,37,93,18,12,77,99,14,22,19,50,2,18,45,63,8,2,89,79,79,7,33,77,18,20,22,12,58,61,20,4,58,20,51,79,14,32,19,87,21,19,76,8,81,7,13,72,75,22,28,22,14,92,30,18,90,10,6,97,25,34,9,20,26,52,45,6,4,97,4,46,26,86,61,20,25,28,26,22,54,69,16,51,3,58,5,23,75,92,18,98,12,11,55,38,22,87,14,20,17,52,73,9,91,30,14,26,12,56,81,54,9,72,18,12,47,93,22,54,21,59,73,7,78,12,87,26,5,39,45,4,55,16,21,86,62,20,98,61,14,20,70,14,25,92,32,44,2,3,15,32,23,23,97,76,78,15,23,95,21,11,69,34,12,89,3,95,24,15,59,38,39,72,14,15,55,48,18,2,43,26,13,58,68,11,22,89,33,79,22,43,40,14,26,5,50,11,28,9,36,33,2,22,43,21,90,15,92,14,14,49,9,80,14,85,99,70,8,16,14,15,70,1,39,32,45,5,57,12,12,4,99,75,28,14,2,28,71,5,69,61,4,28,98,97,87,10,80,2,65,93,6,21,81,7,95,22,35,18,38,23,11,53,14,5,2,84,3,70,33,19,8,52,10,99,14,58,36,1,3,30,53,4,7,47,10,93,2,32,17,40,68,43,20,41,4,16,21,29,23,82,2,18,37,37,15,19,26,41,28,9,95,17,17,52,25,13,49,28,47,22,5,52,14,21,72,83,7,17,86,20,3,18,58,14,19,25,56,65,65,26,53,8,20,75,31,21,40,17,6,33,20,95,47,24,75,26,17,96,24,48,65,97,4,52,20,78,47,14,23,77,32,8,18,98,43,7,61,25,84,40,6,36,24,87,24,71,77,13,20,49,16,60,35,9,64,48,21,2,74,25,1,2,57,11,58,7,45,35,26,13,74,92,2,9,82,9,20,23,15,33,94,7,10,48,78,16,24,94,33,11,21,5,89,47,15,52,12,51,51,81,9,18,39,14,2,97,79,33,23,12,99,3,16,11,79,83,45,18,23,78,86,69,10,25,98,62,62,18,7,44,47,1,3,92,8,22,81,9,3,29,8,81,21,13,95,6,5,99,5,29,16,3,53,72,26,14,44,97,7,43,12,42,65,17,8,12,88,55,18,20,34,13,39,10,72,58,15,11,69,17,94,20,22,52,28,13,30,65,8,2,63,18,4,36,17,8,71,16,71,15,64,14,31,51,75,1,12,92,14,35,23,40,45,1,5,87,28,18,83,43,9,90,2,3,50,18,61,68,5,89,16,44,7,34,82,74,15,83,15,70,13,80,20,43,8,35,14,58,50,75,20,50,9,68,46,52,2,73,11,60,32,61,25,40,9,31,21,73,0,0,21,21,1,10,1,0,0,0,0,0,0]

# -- part 1 -- #
import pygame
import sys
import time
import random

from pygame.locals import *

FPS = 30
pygame.init()
fpsClock=pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0,0,0))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

GRIDSIZE=10
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

screen.blit(surface, (0,0))

def draw_box(surf, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(surf, color, r)


comp = intCodeComp(a)
cells = {}
bot = [500,500]
inp = 1
if __name__ == '__main__':
    while True:
        print(inp)

        key = False
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    inp = 1
                if event.key == K_DOWN:
                    inp = 2
                elif event.key == K_LEFT:
                    inp = 3
                elif event.key == K_RIGHT:
                    inp = 4


        comp.setInputs(inp)
        comp.run()
        update = comp.readOutputs()[0]
        if update == 0:
            inp = (inp % 4) + 1
            if inp == 1:
                cells[(bot[0], bot[1] - 10)] = update
            elif inp == 2:
                cells[(bot[0], bot[1] + 10)] = update
            elif inp == 3:
                cells[(bot[0] - 10, bot[1])] = update
            elif inp == 4:
                cells[(bot[0] + 10, bot[1])] = update
            continue
            
        else:
            if inp == 1:
                bot[1] -= 10
            elif inp == 2:
                bot[1] += 10
            elif inp == 3:
                bot[0] -= 10
            elif inp == 4:
                bot[0] += 10
            cells[(bot[0], bot[1])] = update
        for i in cells:
            if cells[i] == 0:
                draw_box(surface, (255,255,255), i)
            if cells[i] == 1:
                draw_box(surface, (128,128,128), i)
            if cells[i] == 2:
                draw_box(surface, (0,255,0), i)


        inp = ((inp - 2) % 4) + 1
        draw_box(surface, (255,0,0), (bot[0], bot[1]))
        screen.blit(surface, (0,0))
        pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(FPS)
