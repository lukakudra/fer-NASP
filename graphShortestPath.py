#!/usr/bin/env python3

NO_OF_VERTICES = 18

# This is a graph from Zadatci_za_Lab3.pdf
# Zadatci za 11 bodova, 2)
graph = {
    ('a', 'b'): 2,
    ('a', 'c'): 6,
    ('a', 'd'): 12,
    ('b', 'c'): 3,
    ('b', 'e'): 9,
    ('c', 'f'): 1,
    ('d', 'h'): -2,
    ('e', 'g'): 1,
    ('f', 'e'): 2,
    ('f', 'h'): 4,
    ('g', 'i'): 2,
    ('h', 'i'): 3,
    ('h', 'k'): 1,
    ('h', 'l'): -3,
    ('h', 'm'): -2,
    ('i', 'j'): -1,
    ('j', 'n'): 5,
    ('k', 'j'): 1,  # this one has no weight in the picture
    ('k', 'o'): -9,
    ('l', 'm'): 2,
    ('l', 'p'): 7,
    ('m', 'r'): 2,
    ('n', 'o'): 1,  # this one has no weight in the picture
    ('n', 's'): -9,
    ('o', 's'): 11,
    ('p', 's'): -6,
    ('r', 's'): 3
}


# Prints data in a following form:
# src --> dst length: lengthOfPath path: src -> ... -> dst
def printDistances(src, dist, predecessor):
    # print(src + ' --> ' + 'a' + ', length: ' + str(dist['a']) + ', path: ' +
          # getShortestPath(predecessor, src, 'a'))
    print(src + ' --> ' + 'b' + ', length: ' + str(dist['b']) + ', path: ' +
          getShortestPath(predecessor, src, 'b'))
    print(src + ' --> ' + 'c' + ', length: ' + str(dist['c']) + ', path: ' +
          getShortestPath(predecessor, src, 'c'))
    print(src + ' --> ' + 'e' + ', length: ' + str(dist['e']) + ', path: ' +
          getShortestPath(predecessor, src, 'e'))
    print(src + ' --> ' + 'f' + ', length: ' + str(dist['f']) + ', path: ' +
          getShortestPath(predecessor, src, 'f'))
    print(src + ' --> ' + 'g' + ', length: ' + str(dist['g']) + ', path: ' +
          getShortestPath(predecessor, src, 'g'))
    print(src + ' --> ' + 'h' + ', length: ' + str(dist['h']) + ', path: ' +
          getShortestPath(predecessor, src, 'h'))
    print(src + ' --> ' + 'i' + ', length: ' + str(dist['i']) + ', path: ' +
          getShortestPath(predecessor, src, 'i'))
    print(src + ' --> ' + 'j' + ', length: ' + str(dist['j']) + ', path: ' +
          getShortestPath(predecessor, src, 'j'))
    print(src + ' --> ' + 'k' + ', length: ' + str(dist['k']) + ', path: ' +
          getShortestPath(predecessor, src, 'k'))
    print(src + ' --> ' + 'l' + ', length: ' + str(dist['l']) + ', path: ' +
          getShortestPath(predecessor, src, 'l'))
    print(src + ' --> ' + 'm' + ', length: ' + str(dist['m']) + ', path: ' +
          getShortestPath(predecessor, src, 'm'))
    print(src + ' --> ' + 'n' + ', length: ' + str(dist['n']) + ', path: ' +
          getShortestPath(predecessor, src, 'n'))
    print(src + ' --> ' + 'o' + ', length: ' + str(dist['o']) + ', path: ' +
          getShortestPath(predecessor, src, 'o'))
    print(src + ' --> ' + 'p' + ', length: ' + str(dist['p']) + ', path: ' +
          getShortestPath(predecessor, src, 'p'))
    print(src + ' --> ' + 'r' + ', length: ' + str(dist['r']) + ', path: ' +
          getShortestPath(predecessor, src, 'r'))
    print(src + ' --> ' + 's' + ', length: ' + str(dist['s']) + ', path: ' +
          getShortestPath(predecessor, src, 's'))


def getShortestPath(predecessor, src, current):
    path = []
    while current is not src:
        path.append(current)
        current = predecessor[current]

    path.append(src)
    path = list(reversed(path))
    stringPath = ""
    for i in range(len(path) - 1):
        stringPath += path[i] + " -> "

    stringPath += path[len(path) - 1]

    return stringPath


def bellman_ford(src):
    dist = {
        'a': float("Inf"),
        'b': float("Inf"),
        'c': float("Inf"),
        'd': float("Inf"),
        'e': float("Inf"),
        'f': float("Inf"),
        'g': float("Inf"),
        'h': float("Inf"),
        'i': float("Inf"),
        'j': float("Inf"),
        'k': float("Inf"),
        'l': float("Inf"),
        'm': float("Inf"),
        'n': float("Inf"),
        'o': float("Inf"),
        'p': float("Inf"),
        'r': float("Inf"),
        's': float("Inf"),
    }

    dist[src] = 0
    predecessor = {}

    for i in range(NO_OF_VERTICES - 1):
        for vertices, w in graph.items():
            u = vertices[0]
            v = vertices[1]
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u

    for vertices, w in graph.items():
        u = vertices[0]
        v = vertices[1]
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    printDistances(src, dist, predecessor)


def main():
    bellman_ford('a')  # 'a' is the src vertex


if __name__ == "__main__":
    main()
