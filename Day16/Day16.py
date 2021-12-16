class BITSPacket:
    def __init__(self, version, id):
        self.version = version
        self.id = id

    def size(self):
        return 6

    def parseValue(self):
        raise NotImplementedError()


class LiteralPacket(BITSPacket):
    def __init__(self, version, id, data):
        super().__init__(version, id)
        self.data = None
        self.dataSize = None
        self.parseData(data)

    def parseData(self, data):
        half_bytes = []
        pointer = 0
        while pointer < len(data):
            half_bytes.append(data[pointer + 1:pointer + 5])
            if data[pointer] == '0':
                break
            pointer += 5
        self.data = int("".join(half_bytes), 2)
        self.dataSize = len(half_bytes) * 5

    def size(self):
        return super().size() + self.dataSize

    def parseValue(self):
        return self.data


class OpPacket(BITSPacket):
    def __init__(self, version, id, lengthLength, subPackets):
        super().__init__(version, id)
        self.subPackets = subPackets
        self.lengthLength = lengthLength

    def size(self):
        return super().size() + 1 + self.lengthLength + sum(map(lambda x: x.size(), self.subPackets))

    def parseValue(self):
        # sum
        if self.id == 0x0:
            c = 0
            for p in self.subPackets:
                c += p.parseValue()
            return c
        # multiply
        elif self.id == 0x1:
            c = 1
            for p in self.subPackets:
                c *= p.parseValue()
            return c
        # min
        elif self.id == 0x2:
            c = self.subPackets[0].parseValue()
            for p in self.subPackets[1:]:
                c = min(c, p.parseValue())
            return c
        # max
        elif self.id == 0x3:
            c = self.subPackets[0].parseValue()
            for p in self.subPackets[1:]:
                c = max(c, p.parseValue())
            return c
        # gt
        elif self.id == 0x5:
            p1 = self.subPackets[0].parseValue()
            p2 = self.subPackets[1].parseValue()
            return 1 if p1 > p2 else 0
        # lt
        elif self.id == 0x6:
            p1 = self.subPackets[0].parseValue()
            p2 = self.subPackets[1].parseValue()
            return 1 if p1 < p2 else 0
        # eq
        elif self.id == 0x7:
            p1 = self.subPackets[0].parseValue()
            p2 = self.subPackets[1].parseValue()
            return 1 if p1 == p2 else 0
        else:
            raise Exception("Unknown opcode: " + str(self.id))


# returns packet
def parsePacket(data):
    version = int(data[0:3], 2)
    id = int(data[3:6], 2)
    if id == 4:
        return LiteralPacket(version, id, data[6:])
    else:
        subPackets = []
        length_type = int(data[6:7], 2)
        if length_type == 0:
            # 15 bit total length of contained sub-packets
            length = int(data[7:22], 2)
            i = 22
            while i < 22 + length:
                subPackets.append(parsePacket(data[i:]))
                i += subPackets[-1].size()
                if i - 22 >= length:
                    break
            return OpPacket(version, id, 15, subPackets)
        elif length_type == 1:
            # 11 bit total count of contained sub-packets
            length = int(data[7:18], 2)
            i = 18
            for _ in range(length):
                subPackets.append(parsePacket(data[i:]))
                i += subPackets[-1].size()
            return OpPacket(version, id, 11, subPackets)
        else:
            raise Exception("Unknown length type")


def part1(data):
    data = bin(int(data, 16))[2:]
    if len(data) % 4 != 0:
        data = '0' * (4 - len(data) % 4) + data
    p = parsePacket(data)
    return getVersionSum(p)


def getVersionSum(packet):
    if isinstance(packet, LiteralPacket):
        return packet.version
    elif isinstance(packet, OpPacket):
        c = packet.version
        for subPacket in packet.subPackets:
            c += getVersionSum(subPacket)
        return c
    else:
        raise Exception("Unknown packet type")


def part2(data, part1_result):
    data = bin(int(data, 16))[2:]
    if len(data) % 4 != 0:
        data = '0' * (4 - len(data) % 4) + data
    p = parsePacket(data)
    return p.parseValue()


def main():
    with open('inp16.txt', 'r') as f:
        data = f.read()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
