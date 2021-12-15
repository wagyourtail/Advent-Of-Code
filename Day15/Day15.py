# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def printSolution(self, dist):
        return dist[self.V - 1]

    def dijkstra(self, src):

        dist = {}
        dist[src] = 0

        Q = set(range(self.V))

        while len(Q):
            m = 100000000000000000
            u = -1
            for a in dist:
                if a in Q and m > dist[a]:
                    m = dist[a]
                    u = a
            if u == -1:
                u = Q.pop()
                dist[u] = sys.maxsize
            else:
                Q.remove(u)

            for neighbor in self.graph[u]:
                if neighbor in Q:
                    alt = dist[u] + self.graph[u][neighbor]
                    if neighbor not in dist or alt < dist[neighbor]:
                        dist[neighbor] = alt

            # if (len(Q) % 100 == 0):
            #     print(len(Q))

        return self.printSolution(dist)


def part1(data):
    data = [[int(x) for x in a] for a in data]
    ll = len(data) * len(data[0])
    g = Graph(ll)
    g.graph = [[]] * ll
    for i in range(len(data)):
        for j in range(len(data[0])):
            l = i * len(data[0]) + j
            m = {}
            if i - 1 >= 0:
                m[l - len(data[0])] = data[i - 1][j]
            if i + 1 < len(data):
                m[l + len(data[0])] = data[i + 1][j]
            if j - 1 >= 0:
                m[l - 1] = data[i][j - 1]
            if j + 1 < len(data[0]):
                m[l + 1] = data[i][j + 1]
            g.graph[l] = m
    print(ll)
    return g.dijkstra(0)


def part2(data, part1_result):
    data = [[int(x) for x in a] for a in data]
    # extend data
    original_i = len(data[0])
    original_j = len(data)

    # extend right
    for _ in range(1, 5):
        for j in range(len(data)):
            data[j] += [x - 9 if x > 9 else x for x in [x + 1 for x in data[j][-original_i:]]]

    # extend down
    for _ in range(1, 5):
        for j in range(original_j):
            data.append([x - 9 if x > 9 else x for x in [x + 1 for x in data[-original_j]]])

    # print(*["".join(i for i in map(str, x)) for x in data], sep='\n')

    # do part 1 on it
    ll = len(data) * len(data[0])
    g = Graph(ll)
    g.graph = [{}] * ll
    for i in range(len(data)):
        for j in range(len(data[0])):
            l = i * len(data[0]) + j
            m = {}
            if i - 1 >= 0:
                m[l - len(data[0])] = data[i - 1][j]
            if i + 1 < len(data):
                m[l + len(data[0])] = data[i + 1][j]
            if j - 1 >= 0:
                m[l - 1] = data[i][j - 1]
            if j + 1 < len(data[0]):
                m[l + 1] = data[i][j + 1]
            g.graph[l] = m
    print(ll)
    return g.dijkstra(0)


def main():
    with open('inp15.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print("wait 18 minutes....")
    print('Part 2: {}'.format(part2(data, 0)))


if __name__ == "__main__":
    main()
