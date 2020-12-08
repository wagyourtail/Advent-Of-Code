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

a = [3,8,1005,8,332,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,28,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,51,1,1103,5,10,1,1104,9,10,2,1003,0,10,1,5,16,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,88,1006,0,2,1006,0,62,2,8,2,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,121,1006,0,91,1006,0,22,1006,0,23,1006,0,1,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,155,1006,0,97,1,1004,2,10,2,1003,6,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,187,1,104,15,10,2,107,9,10,1006,0,37,1006,0,39,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,223,2,2,17,10,1,1102,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,276,1006,0,84,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,301,2,1009,9,10,1006,0,10,2,102,15,10,101,1,9,9,1007,9,997,10,1005,10,15,99,109,654,104,0,104,1,21102,1,936995738516,1,21101,0,349,0,1105,1,453,21102,1,825595015976,1,21102,1,360,0,1105,1,453,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,46375541763,1,1,21101,0,407,0,1105,1,453,21102,1,179339005019,1,21101,0,418,0,1106,0,453,3,10,104,0,104,0,3,10,104,0,104,0,21102,825012036372,1,1,21102,441,1,0,1105,1,453,21101,988648461076,0,1,21101,452,0,0,1105,1,453,99,109,2,22102,1,-1,1,21102,40,1,2,21102,484,1,3,21101,0,474,0,1106,0,517,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,479,480,495,4,0,1001,479,1,479,108,4,479,10,1006,10,511,1102,1,0,479,109,-2,2105,1,0,0,109,4,2102,1,-1,516,1207,-3,0,10,1006,10,534,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,553,1,0,1106,0,558,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,581,2207,-4,-2,10,1006,10,581,22102,1,-4,-4,1105,1,649,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,0,600,0,1105,1,558,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,619,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,641,22102,1,-1,1,21102,1,641,0,106,0,516,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

panels = {}
coords = [0, 0]
facing = 0
comp = intCodeComp(a)
inputs = 0
while not comp.halt:
    if tuple(coords) not in panels:
        inputs = 0
    else:
        inputs = panels[tuple(coords)]
    comp.setInputs(inputs)
    comp.run()
    outputs = comp.readOutputs()
    panels[tuple(coords)] = outputs[0]
    facing += 1 if outputs[1] else -1
    if facing % 4 == 0:
        coords[0] -= 1
    elif facing % 4 == 1:
        coords[1] += 1
    elif facing % 4 == 2:
        coords[0] += 1
    elif facing % 4 == 3:
        coords[1] -= 1
    
    
print(len(panels.keys()))

# -- part 2 -- #
panels = {}
coords = [0, 0]
facing = 0
comp = intCodeComp(a)
inputs = 0
comp.setInputs(1)
while not comp.halt:
    comp.run()
    outputs = comp.readOutputs()
    panels[tuple(coords)] = outputs[0]
    facing += 1 if outputs[1] else -1
    if facing % 4 == 0:
        coords[0] -= 1
    elif facing % 4 == 1:
        coords[1] += 1
    elif facing % 4 == 2:
        coords[0] += 1
    elif facing % 4 == 3:
        coords[1] -= 1
    if tuple(coords) not in panels:
        inputs = 0
    else:
        inputs = panels[tuple(coords)]
    comp.setInputs(inputs)

import turtle

def draw(tt, y, x, color):
    y = -y
    tt.color(color)
    tt.goto(x*5-250,y*5+250)
    tt.pd()
    tt.forward(4)
    tt.left(90)
    tt.forward(4)
    tt.left(90)
    tt.forward(4)
    tt.left(90)
    tt.forward(4)
    tt.left(90)
    tt.penup()

tt = turtle.Turtle()
tt.speed(0)
tt.penup()

for point in panels:
    if panels[point]:
        draw(tt,point[0],point[1], "black")
