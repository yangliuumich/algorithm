# k-clustering
#filename = 'clustering_small.txt'
filename = 'clustering1.txt'
with open(filename) as f:
    g = f.readlines()

k = 4
n = int(g[0])
graph = []
for line in g[1:]:
    start, end, cost = [int(i) for i in line.split(' ')]
    graph.append((start, end, cost))

#graph = [(start, end, cost), ...] 
graph.sort(key = lambda element: element[2])

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
   
def k_clustering(k, graph, union_list):
    cluster = len([size for size in treesize if size>0])
    edges = graph 
    while cluster >  k:
        union(edges[0][0],edges[0][1])
        edges = edges[1:]
        cluster = len([size for size in treesize if size>0])
    while find(edges[0][0]) == find(edges[0][1]):
        edges = edges[1:]
    return edges[0]    
    
print k_clustering(k, graph, union_list)
