
import threading
class intCodeComp(threading.Thread):
    def __init__(self, code):
        self.code = code[:]
        self.inputs = []
        self.outputs = []
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
                self.code[self.code[i + 3]] = self.code[self.code[i + 1] if ip[0] == "0" else i + 1] + self.code[self.code[i + 2] if ip[1] == "0" else i + 2]
                i += 4
            elif opc == 2:
                self.code[self.code[i + 3]] = self.code[self.code[i + 1] if ip[0] == "0" else i + 1] * self.code[self.code[i + 2] if ip[1] == "0" else i + 2]
                i += 4
            elif opc == 3:
                #print("in")
                if inv == len(self.inputs):
                    self.i = i
                    self.awaitInput = True
                    return
                self.awaitInput = False
                self.code[self.code[i + 1]] = int(self.inputs[inv])
                inv += 1
                i += 2
            elif opc == 4:
                #print("out")
                self.outputs.append(self.code[self.code[i+1] if ip[0] == "0" else i + 1])
                i += 2
            elif opc == 5:
                if self.code[(self.code[i + 1] if ip[0] == "0" else i + 1)] != 0:
                    i = self.code[self.code[i + 2] if ip[1] == "0" else i + 2]
                else:
                    i += 3
            elif opc == 6:
                if not self.code[(self.code[i + 1] if ip[0] == "0" else i + 1)] != 0:
                    i = self.code[self.code[i + 2] if ip[1] == "0" else i + 2]
                else:
                    i += 3
            elif opc == 7:
                if self.code[self.code[i + 1] if ip[0] == "0" else i + 1] < self.code[self.code[i + 2] if ip[1] == "0" else i + 2]:
                    self.code[self.code[i + 3]] = 1
                else:
                    self.code[self.code[i + 3]] = 0
                i += 4
            elif opc == 8:
                if self.code[self.code[i + 1] if ip[0] == "0" else i + 1] == self.code[self.code[i + 2] if ip[1] == "0" else i + 2]:
                    self.code[self.code[i + 3]] = 1
                else:
                    self.code[self.code[i + 3]] = 0
                i += 4
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




code = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]
from itertools import permutations

# -- part 1 -- #
e = []
for i in permutations([0,1,2,3,4]):
    output = 0
    #print(i)
    for j in i:
        #print(j)
        comp = intCodeComp(code)
        comp.setInputs(j, output)
        comp.run()
        [output] = comp.readOutputs()
    e.append(output)
print(max(e))

# -- part 2 -- #
e = []
for i in permutations([5,6,7,8,9]):
    comps = [intCodeComp(code), intCodeComp(code), intCodeComp(code), intCodeComp(code), intCodeComp(code)]
    it = 0
    output = 0
    for j in i:
        #print(it)
        comps[it].setInputs(j, output)
        comps[it].run()
        output = comps[it].readOutputs()[0]
        it = (it + 1) % 5
    it = 0
    while True:
        if comps[it].halt:
            break
        comps[it].setInputs(output)
        comps[it].run()
        output = comps[it].readOutputs()[0]
        it = (it + 1) % 5
    e.append(output)

print(max(e))
