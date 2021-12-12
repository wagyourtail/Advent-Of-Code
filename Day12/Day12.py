import statistics
from collections import defaultdict


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def isBig(self):
        return self.name == self.name.upper()

    def pathsToEnd(self, path=None):
        if path is None:
            path = [self]

        paths = []

        if self.name == 'end':
            return [path]

        for connection in self.connections:
            if connection.name != 'start' and (connection not in path or connection.isBig()):
                path2 = path[:]
                path2.append(connection)
                paths += connection.pathsToEnd(path2)

        return paths

    def pathToEndOneSmallTwice(self, path=None):
        if path is None:
            path = [self]

        paths = []

        if self.name == 'end':
            return [path]

        small_conns = [conn for conn in path if not conn.isBig()]
        if len(small_conns) and small_conns.count(statistics.mode(small_conns)) == 2:
            small_conns = []
        for connection in self.connections:
            if connection.name != 'start' and (connection not in path or connection.isBig()):
                path2 = path[:]
                path2.append(connection)
                paths += connection.pathToEndOneSmallTwice(path2)
            elif len(small_conns) and not connection.isBig() and connection.name != 'start' and small_conns.count(connection) == 1:
                    path2 = path[:]
                    path2.append(connection)
                    paths += connection.pathToEndOneSmallTwice(path2)

        return paths

def getOrSet(dict, key):
    if key not in dict:
        dict[key] = Cave(key)
    return dict[key]

def part1(data):
    caves = {}
    for i in data:
        i = i.split('-')
        getOrSet(caves, i[0]).add_connection(getOrSet(caves, i[1]))
        getOrSet(caves, i[1]).add_connection(getOrSet(caves, i[0]))

    paths = caves['start'].pathsToEnd()

    # for path in sorted([",".join([connection.name for connection in path]) for path in paths]):
    #     print(path)

    return len(paths)


def part2(data, part1_result):
    caves = {}
    for i in data:
        i = i.split('-')
        getOrSet(caves, i[0]).add_connection(getOrSet(caves, i[1]))
        getOrSet(caves, i[1]).add_connection(getOrSet(caves, i[0]))

    paths = caves['start'].pathToEndOneSmallTwice()

    # for path in sorted([",".join([connection.name for connection in path]) for path in paths]):
    #     print(path)

    return len(paths)


def main():
    with open('inp12.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
