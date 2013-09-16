#Prim's Minimum Spanning Tree Algorithm
filename = 'MST.txt'
#filename = 'primcase.txt'
#filename = 'prim_easycase.txt'
with open(filename) as f:
    g = f.read().splitlines()

# n = #of vertices, m = #of edges
n = int(g[0].split(' ')[0])
m = int(g[0].split(' ')[1])

#graph[key] = [[end, cost], []...]     
graph = {}

for i in range(1, n+1):
    graph[i] = []

for line in g[1:]:
    [start, end, cost] = [int(a) for a in line.split(' ')]
    graph[start].append([end, cost])
    graph[end].append([start, cost])

for key in graph:
    graph[key].sort(key = lambda element:element[1])

def prim(graph):
    v = set()
    for i in range(1, n+1):
        v.add(i)
    x = set([1])
    t = set()
    while x != v:
        current_cheapest = None
        for xv in x:
            cheapest = None
            for [end, cost] in graph[xv]:
                if end in x:                    
                    continue
                else:
                    cheapest = (end, cost)
                    break
            if cheapest == None:
                continue
            else:
                if current_cheapest == None or cheapest[1] < current_cheapest[1]:
                    current_cheapest = cheapest
        t.add(current_cheapest)
        x.add(current_cheapest[0]) 
    total_cost = 0
    for (end, cost) in t:
        total_cost += cost
    return total_cost 

print prim(graph)
