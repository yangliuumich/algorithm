#k-clustering with hamming distance
filename = 'clustering_big.txt'
#filename = 'clustering_hamming.txt'
with open(filename) as f:
    g = f.readlines()

n = int(g[0].split(' ')[0])
bit = int(g[0].split()[1])
max_distance = 2
#graph[key] = [1,1,1,....]
graph = {}
for i in range(1, n+1):
    graph[i] = [int(b) for b in g[i].split()]

def distance(a, b):
    d = 0
    for i in range(bit):
        if graph[a][i] != graph[b][i]:
            d += 1
    return d

union_list = []
for i in range(1, n+1):
    union_list.append(i)

treesize = []
for i in range(n):
    treesize.append(1)

def find(a):
    root = a
    while root != union_list[root-1]:
        union_list[root-1] = union_list[union_list[root-1]-1]
        root = union_list[root-1]
    return root

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if treesize[root_a-1] > treesize[root_b-1]:
            root_a, root_b = root_b, root_a
        union_list[root_a-1] = root_b
        treesize[root_b-1] += treesize[root_a-1]
        treesize[root_a-1] = 0

def flip(node, x):
    def reverse(a):
        if a == 0:
            return 1
        return 0

    results = []
    if x == 1: 
        for i in range(bit):
            new = [b for b in node]
            new[i] = reverse(new[i])
            results.append(new)
    elif x == 2:
        for i in range(bit-1):
            for j in range(i+1,bit):
                new = [b for b in node]
                new[i] = reverse(new[i])
                new[j] = reverse(new[j])
                results.append(new)
    return results  

edges = {}
for i in range(max_distance + 1):
    edges[i] = []

for i in range(1, n+1):
    d_0 = [(i, item) for (key, item) in graph.items() if key > i and item == graph[i]]
    d_1 = [(i, item) for (key, item) in graph.items() if key > i and item in flip(graph[i], 1)]
    d_2 = [(i, item) for (key, item) in graph.items() if key > i and item in flip(graph[i], 2)]
    edges[0] += d_0
    edges[1] += d_1
    edges[2] += d_2

for i in range(max_distance+1):
    for edge in edges[i]:
        union(edge[0], edge[1])

print len([size for size in treesize if size > 0])
