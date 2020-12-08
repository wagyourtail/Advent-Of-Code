a = """12 JSMPL, 1 RFSHT => 8 NLTCF
6 LTSZQ, 22 KLSMX, 12 CWLGT => 2 MZXFC
4 WMVD, 3 PLBT, 1 ZKDMR => 5 CWLGT
5 SDTGC => 2 LSFKV
189 ORE => 3 TNTDN
20 CZKW => 4 BGNFD
5 XFMH => 7 SFRQ
7 NLTCF => 1 KLSMX
1 NLTCF => 4 HTDFH
2 RFPT, 5 JFXPH => 5 KRCQ
178 ORE => 7 XGLBX
1 NHQH => 3 NDMT
4 BNVTZ, 13 KXFJ, 14 QRBK, 56 SJSLP, 18 SPFP, 9 WMVD, 12 JFXPH, 1 MHXF => 1 FUEL
1 XQRX, 2 DPRVM, 1 HTDFH, 24 NLTCF, 8 SPBXP, 20 TSRNS, 2 VJDBK, 1 PXKL => 7 SPFP
6 WMVD => 3 SPBXP
1 XGLBX => 8 QXLMV
1 PLBT => 5 ZKDMR
25 VJDBK, 5 MZXFC, 3 BDGCJ => 9 BNVTZ
2 TNTDN, 1 SZNCS => 2 LMXBH
3 TNTDN => 6 RVRD
4 RFPT => 6 VHMQ
7 QXLMV, 1 LMXBH, 4 CSZP => 8 XFMH
5 SZNCS => 5 JSMPL
5 MHXF, 5 LTSZQ => 4 RFPT
5 XQMBJ, 1 BGNFD, 5 TQPGR => 3 NHQH
10 CHWS => 2 BDGCJ
19 DPRVM, 13 NHQH, 7 CZKW => 6 FWMXM
1 KLSMX, 1 PLBT, 5 XFMH => 3 SDTGC
20 LMXBH => 9 RFSHT
3 XGLBX => 1 TNPVZ
3 FBWF => 7 WMVD
1 QXLMV, 1 LMXBH => 3 ZMNV
5 JSMPL, 12 SFRQ => 8 CZKW
2 TNPVZ => 9 MHXF
2 MNVX, 1 RBMLP, 6 LSFKV => 9 VJDBK
26 SZNCS, 1 XGLBX => 6 CSZP
6 FBWF, 2 SPBXP, 4 BDGCJ => 2 TQPGR
5 LSFKV, 5 DPRVM => 9 QNFC
33 BDGCJ, 3 CWLGT => 4 XQRX
2 TQPGR, 22 LSFKV, 2 RFPT, 1 BDGCJ, 1 ZKDMR, 7 TSRNS, 6 DPRVM, 11 KRCQ => 2 QRBK
13 XQRX, 3 FWMXM, 2 CWLGT, 1 XQMBJ, 3 BGNFD, 6 HTDFH, 10 TSRNS => 5 KXFJ
1 ZKDMR => 9 CHWS
14 MNVX, 5 XFMH => 7 LTSZQ
2 NDMT, 2 QNFC, 11 ZMNV => 6 PXKL
7 SFRQ => 5 MNVX
2 WMPKD, 1 QXLMV => 9 SJSLP
14 JFXPH => 3 XQMBJ
14 SFRQ => 7 FBWF
1 WMPKD, 30 GBQGR, 4 SPBXP => 9 DPRVM
129 ORE => 4 SZNCS
5 JSMPL => 8 JFXPH
9 JFXPH, 2 VHMQ => 5 RBMLP
6 JSMPL => 7 GBQGR
25 SFRQ, 19 HRMT => 5 WMPKD
3 ZMNV => 9 PLBT
7 ZMNV, 9 RVRD, 8 SFRQ => 7 HRMT
8 RBMLP => 6 TSRNS"""

# -- formatting and class -- #
import re, math

a = [[c.split(',') for c in b.split('=>')] for b in a.split('\n')]
materials = {}
processed = {"ORE":1000000000000}

class mat(object):
    def __init__(self, name, recipie_inp, q_out):
        self.name = name
        self.recipie = recipie_inp
        self.q_out = q_out
    def doRecipie(self, qty):
        for i in self.recipie:
            while processed[i] < self.recipie[i] * math.ceil(qty/self.q_out):
                if (i == "ORE"):
                    return False
                if not materials[i].doRecipie(self.recipie[i] * math.ceil(qty/self.q_out) - processed[i]):
                    return False
        for i in self.recipie:
            processed[i] -= self.recipie[i] * math.ceil(qty/self.q_out)
        processed[self.name] += self.q_out * math.ceil(qty/self.q_out)
        return True
    def deCraft(self, qty):
        if self.q_out * math.floor(qty/self.q_out) < processed[self.name]:
            return False
        for i in self.recipie:
            processed[i] += self.recipie[i] * math.floor(qty/self.q_out)
        processed[self.name] -= self.q_out * math.floor(qty/self.q_out)
        return True
            
for i in a:
    ins = i[0]
    out = i[1][0]
    recipie = {}
    for j in ins:
        m = re.search(r'(\d+) ([^\s]+)', j)
        recipie[m.group(2)] = int(m.group(1))
    m = re.search(r'(\d+) ([^\s]+)', out)
    materials[m.group(2)] = mat(m.group(2), recipie, int(m.group(1)))
    processed[m.group(2)] = 0

# -- part 1 -- #
materials["FUEL"].doRecipie(1)
print(1000000000000-processed["ORE"])

# -- part 2 -- #
batch = 10000
while batch > 0:
    print(batch)
    while materials["FUEL"].doRecipie(batch):
        pass
    batch -= 1
    print(batch)
    change = True
    while change:
        change = False
        for i in materials:
            if i != "FUEL":
                if materials[i].deCraft(processed[i]):
                    change = True
print(processed["FUEL"])
